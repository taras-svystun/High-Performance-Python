from check_prime import slow_prime, medium_prime, fast_prime
from time import time
from multiprocessing import Pool
from itertools import compress

if __name__ == '__main__':
    # Fast primes + multiprocessing
    pool = Pool()
    start = time()
    numbers = range(4, 10 ** 6)
    flags = pool.map(fast_prime, numbers)
    primes = [prime for prime in compress(numbers, flags)]
    print(f'Multi time: {round(time() - start, 3)} sec')

    # Fast primes without multiprocessing
    fast = []
    start = time()
    for number in numbers:
        if fast_prime(number):
            fast.append(number)
    print(f'NoMulti Fast time: {round(time() - start, 3)} sec')
    print(fast == primes)
