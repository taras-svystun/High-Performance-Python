import unittest
from unittest import result

if '__builtins__' not in dir() or not hasattr(__builtins__, 'profile'):
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner

@profile
def random_function(param):
    return param ** 2

class TestCase(unittest.TestCase):
    def test(self):
        result = random_function(5)
        self.assertEquals(result, 25)