import numpy as np
from time import time

def slow_prime(number: int) -> bool:
    start, end = 2, int(np.sqrt(number)) + 1
    for divider in range(start, end):
        if number % divider == 0:
            return False
    return True

def medium_prime(number: int) -> bool:
    if number % 2 == 0:
        return False
    start, end = 3, int(np.sqrt(number)) + 1
    for divider in range(start, end, 2):
        if number % divider == 0:
            return False
    return True

def fast_prime(number: int) -> bool:
    if number % 2 == 0 or number % 3 == 0:
        return False
    start, end = 3, int(np.sqrt(number)) + 1
    for divider in range(start, end, 6):
        if number % (divider + 2) == 0 or number % (divider + 4) == 0:
            return False
    return True

if __name__ == '__main__':
    slow, medium, fast = [], [], []
    start = time()
    for number in range(4, 10 ** 6):
        if slow_prime(number):
            slow.append(number)
    print(f'Slow time: {round(time() - start, 3)} sec')

    start = time()
    for number in range(4, 10 ** 6):
        if medium_prime(number):
            medium.append(number)
    print(f'Medium time: {round(time() - start, 3)} sec')
    
    start = time()
    for number in range(4, 10 ** 6):
        if fast_prime(number):
            fast.append(number)
    print(f'Fast time: {round(time() - start, 3)} sec')
    print('Results equal' if slow == medium == fast else 'NOT equal results')
