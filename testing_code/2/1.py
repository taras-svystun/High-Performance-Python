from time import time
from numpy import sqrt
import numpy as np
import cProfile
import pstats
from line_profiler import LineProfiler

np.random.seed(1)

def time_decorator(func):
    def inner(*args, **kwargs):
        now = time()
        result = func(*args, **kwargs)
        time_passed = time() - now
        print(f'Execution time of {inner.__name__} is {round(time_passed, 8)} second')
        return result
    return inner

@time_decorator
def random_function(n, spread):
    '''
    It is not a serious function, it just contains random
    commands, which I was testing.
    '''
    numbers = list(map(int, np.random.rand(n) * spread))
    info = dict.fromkeys(numbers, 0)
    for number in numbers:
        ndivisors, nnotdivisors = 1, 0
        divisors = [1]
        for i in range(2, int(number) + 1):
            if number % i:
                nnotdivisors += 1
            else:
                ndivisors += 1
                for j in range(100):
                    divisors.append(i)
        info[number] = ndivisors, nnotdivisors, divisors
    return info

def random_function2():
    lst = []
    result = []
    for i in range(10 ** 6):
        lst.append(i)
    for elem in lst:
        if not elem % 2:
            result.append(elem)
    for flag in range(100):
        result.sort(reverse=flag%2)
    return result

if __name__ == '__main__':
    # cProfile.run('random_function2()')
    # python -m cProfile -o profile.stats testing_code/two.py
    # p = pstats.Stats('profile.stats')
    # p.sort_stats('cumulative')
    # p.print_stats()
    # p.print_callers()
    # p.print_callees()
    
    # lp = LineProfiler()
    # lp_wrapper = lp(random_function2)
    # lp.print_stats()
    # random_function2()

    # profile = LineProfiler(random_function2)
    # profile.print_stats()
    pass