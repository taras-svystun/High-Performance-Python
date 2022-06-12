# cython -a time_test.pyx 
# to see the html output

# for more speedups
# https://nealhughes.net/cython1/

from time import time

def test(int times):
    cdef double start = time()
    cdef int counter = 0
    cdef int i;
    for i in range(times):
        if i % 2 == 0:
            counter += i
        else:
            counter -= i
    print(time() - start)
    print(counter)

if __name__ == '__main__':
    test(10**8)
