from cgi import test
from time import time
from numpy import sqrt
import numpy as np
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
def check_prime(n, spread):
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
                divisors.append(i)
        info[number] = ndivisors, nnotdivisors, divisors
    return info

if __name__ == '__main__':
    # check_prime(test)
    pass