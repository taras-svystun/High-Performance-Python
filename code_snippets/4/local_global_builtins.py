import math
from math import sin
from time import time

def slow():
    for i in range(2 * 10**7):
        math.sin(i)

def medium():
    for i in range(2 * 10**7):
        sin(i)

def fast(sin=math.sin):
    for i in range(2 * 10**7):
        sin(i)

def final():
    local_sin = math.sin
    for i in range(2 * 10**7):
        local_sin(i)

start = time()
slow()
print(f'After slow: {round(time() - start, 2)} sec.') # 1.52 sec
start = time()
medium()
print(f'After slow: {round(time() - start, 2)} sec.') # 1.13 sec
start = time()
fast()
print(f'After slow: {round(time() - start, 2)} sec.') # 1.04 sec
start = time()
final()
print(f'After slow: {round(time() - start, 2)} sec.') # 1.04 sec