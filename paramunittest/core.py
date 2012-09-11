import unittest
import collections

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

def parametrized(parameters_seq):
    parameters_seq = _process_parameters(parameters_seq)




class ParamTestCase(unittest.TestCase):
    pass