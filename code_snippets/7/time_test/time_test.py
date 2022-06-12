# cython -a time_test.pyx 
# to see the html output

from time import time

def test(times):
    start = time()
    counter = 0
    for i in range(times):
        if not i % 2:
            counter += i
        else:
            counter -= i
    print(time() - start)

if __name__ == '__main__':
    test(10**8)
