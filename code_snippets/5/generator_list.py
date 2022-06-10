from time import time
from sys import getsizeof

k = 10 ** 6

start = time()
lst = [i for i in range(k) if not i % 3]
result1 = len(lst)

start = time()
generator = (1 for i in range(k) if not i % 3)
result2 = sum(generator)

print(f'Results the same: {result1 == result2}', f'\nSize of list: {getsizeof(lst)}\
\nSize of generator: {getsizeof(generator)}')