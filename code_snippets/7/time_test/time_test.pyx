# cython -a time_test.pyx 
# to see the html output

# for more speedups
# https://nealhughes.net/cython1/

from time import time

def test(int times):
    start = time()
    cdef int counter = 0, i;
    for i in range(times):
        if i % 2:
            counter += i
        else:
            counter -= i
    print(time() - start)
    return counter

if __name__ == '__main__':
    test(10**8)
