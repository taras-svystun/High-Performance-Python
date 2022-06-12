# https://numba.readthedocs.io/en/stable/user/5minguide.html

import numpy as np
from numba import jit
from time import time

def slow(times=10**8):
    counter = 0
    for i in range(times):
        counter += 1.3
        counter -= 1.30001
    return counter

@jit(nopython=True)
def fast(times=10**8):
    counter = 0
    for i in range(times):
        counter += 1.3
        counter -= 1.30001
    return counter


if __name__ == '__main__':
    start = time()
    slow()
    print(time() - start)

    start = time()
    fast()
    print(time() - start)
    start = time()
    fast()
    print(time() - start)
