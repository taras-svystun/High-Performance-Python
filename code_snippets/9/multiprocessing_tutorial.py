from multiprocessing import Pool, Process, Lock, Value, Array
import os

import multiprocessing as mp


def f1(x):
    return x ** 2

def f2(x, y):
    return x ** 2 + y ** 2

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f3(name):
    info('function f3')
    print('hello', name)

def foo(q, param):
    for i in range(param):
        q.put(i)

def f4(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

def f5(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    pool = Pool()
    test1 = list(range(1, 9))
    print(pool.map(f1, test1))

    test2 = [(i, i + 1) for i in range(1, 9, 2)]
    print(pool.starmap(f2, test2))

    info('main line')
    p = Process(target=f3, args=('bob',))
    p.start()
    p.join()

    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,10))
    p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    p.join()

    # lock = Lock()
    # for num in range(10):
    #     Process(target=f4, args=(lock, num)).start()

    num = Value('d', 0.0)
    arr = Array('i', range(10))
    print(num.value)
    print(arr[:])

    p = Process(target=f5, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
