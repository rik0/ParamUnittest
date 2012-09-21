import copy
import unittest
import collections
import importlib
from unittest.util import strclass

__all__ = [
    'parametrized',
    'ParametrizedTestCase',
]

def _process_parameters(parameters_seq):
    processed_parameters_seq = []
    for parameters in parameters_seq:
        if isinstance(parameters, collections.Mapping):
            processed_parameters_seq.append((tuple(),
                                             dict(parameters)))
        elif (len(parameters) == 2
              and isinstance(parameters[0], collections.Sequence)
              and isinstance(parameters[1], collections.Mapping)):
            processed_parameters_seq.append((tuple(parameters[0]),
                                             dict(parameters[1])))
        else:
            processed_parameters_seq.append((tuple(parameters),
                                             dict()))
    return processed_parameters_seq


def _build_name(name, index):
    return '%s_%d' % (name, index)


class ParametrizedTestCase(unittest.TestCase):
    def setParameters(self, *args, **kwargs):
        raise NotImplementedError(
            ('setParameters must be implemented '
             'because it receives the parameters.'))

    def getParameters(self):
        """
        Return the parameters with which this test case was instantiated.
        """
        raise NotImplementedError(
            'getParameters should have been patched by parametrized.')

    def getFullParametersSequence(self):
        raise NotImplementedError(
            'getFullParametersSequence should have been patched by parametrized.')

    def getTestCaseIndex(self):
        """
        Return the index of the current test case according to the list of
        parametes passed to parametrized.
        """
        raise NotImplementedError(
            'getTestCaseIndex should have been patched by parametrized.')

    def getFullParametersSequence(self):
        """
        Return the full normalized list of parameters passed to parametrized.
        """
        raise NotImplementedError(
            'getFullParametersSequence should have been patched by parametrized.')

    def __str__(self):
        return "%s[%d](%s) (%s)" % (self._testMethodName,
                                    self.getTestCaseIndex(),
                                    self.getParameters(),
                                    strclass(self.__class__))

    def __repr__(self):
        return "<%s[%d](%s) testMethod=%s>" % (strclass(self.__class__),
                                               self.getTestCaseIndex(),
                                               self.getParameters(),
                                               self._testMethodName)


def parametrized(*parameters_seq):
    parameters_seq = _process_parameters(parameters_seq)
    def magic_module_set_test_case(cls):
        if not hasattr(cls, 'setParameters'):
            raise TypeError('%s does not have a setParameters method.' % (
                cls.__name__, ))
        module = importlib.import_module(cls.__module__)
        for index, parameters in enumerate(parameters_seq):
            name = _build_name(cls.__name__, index)
            def closing_over(parameters=parameters, index=index):
                def setUp(self):
                    self.setParameters(*parameters[0], **parameters[1])
                    cls.setUp(self)
                def getParameters(self):
                    """
                    Return the parameters with which this test case was instantiated.
                    """
                    return parameters
                def getTestCaseIndex(self):
                    """
                    Return the index of the current test case according to the list of
                    parametes passed to parametrized.
                    """
                    return index
                def getFullParametersSequence(self):
                    """
                    Return the full normalized list of parameters passed to parametrized.
                    """
                    return copy.copy(parameters_seq)
                return setUp, getParameters, getTestCaseIndex, getFullParametersSequence
            (set_up, get_parameters,
             get_test_case_index,
             get_full_parameters_sequence) = closing_over()
            new_class = type(name, (cls, ),
                             {'setUp': set_up,
                              'getParameters': get_parameters,
                              'getTestCaseIndex': get_test_case_index,
                              'getFullParametersSequence': get_full_parameters_sequence})
            setattr(module, name, new_class)
        return None # this is explicit!
    return magic_module_set_test_case
