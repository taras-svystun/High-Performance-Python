import numpy as np
from numba import jit, njit
from time import time

def slow(times=10**6):
    counter = 0
    for i in range(times):
        counter += np.sin(i)
        counter -= np.cos(i)
        counter += np.pi
        counter -= 1.15 * np.e
        counter = np.tanh(counter)
    return counter

@njit(fastmath=True)
def fast(times=10**6):
    counter = 0
    for i in range(times):
        counter += np.sin(i)
        counter -= np.cos(i)
        counter += np.pi
        counter -= 1.15 * np.e
        counter = np.tanh(counter)
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
