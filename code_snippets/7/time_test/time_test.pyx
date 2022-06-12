# cython -a time_test.pyx 
# to see the html output

# for more speedups
# https://nealhughes.net/cython1/

from time import time

def test(int num):
    cdef double start = time()
    cdef int counter = 0
    cdef int times = num
    for i in range(times):
        if i % 2 == 0:
            counter = counter + i
        else:
            counter = counter - i
    print(time() - start)

if __name__ == '__main__':
    test(10**8)
