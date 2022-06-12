from setuptools import setup
from Cython.Build import cythonize

setup(
    name='time_testing',
    ext_modules = cythonize("time_test.pyx")
)
