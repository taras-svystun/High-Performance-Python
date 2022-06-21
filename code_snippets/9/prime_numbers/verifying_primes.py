import numpy as np
from time import time
from multiprocessing import Pool

def time_decorator(func):
    def inner(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took: {round(time() - start, 3)} sec.')
        return result
    return inner


@time_decorator
def prime_serial(number: int):
    if number % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def prime_in_range(number, start_end):
    start, end = start_end
    if number % 2 == 0:
        return False
    assert(start % 2 != 0)
    for i in range(start, int(end), 2):
        if number % i == 0:
            return False
    return True

@time_decorator
def prime_naive_pool(number: int, pool, n_workers: int = 8):
    start = 3
    end = int(np.sqrt(number)) + 1
    ranges_to_check = [(array[0], array[-1]) for array in 
    np.array_split(list(range(start, end)), n_workers)]
    ranges_to_check = zip([number] * n_workers, ranges_to_check)
    print(list(ranges_to_check))
    result = pool.map(prime_in_range, ranges_to_check)
    if False in result:
        return False
    return True
    return all(result)


if __name__ == '__main__':
    NOT_PRIME = 100109100129100369
    test = 149309 * 50
    print(prime_serial(test))
    pool = Pool(8)
    print(prime_naive_pool(test, pool))
