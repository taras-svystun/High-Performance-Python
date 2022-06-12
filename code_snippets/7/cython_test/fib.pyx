# from __futuire__ import print_function
import cython
from time import time

def fib(n):
    """Print the Fibonacci series up to n."""
    start = time()
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
    print(time() - start)
