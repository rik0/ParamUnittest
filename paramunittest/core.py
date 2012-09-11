import unittest
import collections
import importlib
import exceptions
import sys

def _process_parameters(parameters_seq):
    processed_parameters_seq = []
    for parameters in parameters_seq:
        if isinstance(parameters, collections.Mapping):
            processed_parameters_seq.append((tuple(), dict(parameters)))
        elif (len(parameters) == 2
              and isinstance(parameters[0], collections.Sequence)
              and isinstance(parameters[1], collections.Mapping)):
            processed_parameters_seq.append((tuple(parameters[0]), dict(parameters[1])))
        else:
            processed_parameters_seq.append((tuple(parameters), dict()))
    return processed_parameters_seq

class ParametrizedTestCase(unittest.TestCase):
    def __init__(self):
        raise NotImplementedError('__init__ must be implemented because it receives the parameters.')

def parametrized(*parameters_seq):
    parameters_seq = _process_parameters(parameters_seq)
    def magic_module_set_test_case(cls):
        if not issubclass(cls, ParametrizedTestCase):
            raise TypeError('%s does not subclass %s' % (cls.__name__, ParametrizedTestCase.__name__))
        module = importlib.import_module(cls.__module__)
#        import sys
#        print >> sys.stderr, cls
#        print >> sys.stderr, cls.__module__
#        print >> sys.stderr, importlib.import_module(cls.__module__)
#        print >> sys.stderr, dir(cls)
        return None # this is explicit!
    return magic_module_set_test_case
