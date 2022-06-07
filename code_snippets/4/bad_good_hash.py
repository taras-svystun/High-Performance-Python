from string import ascii_lowercase
from time import time

class BadHash(str):
    def __hash__(self) -> int:
        return 42

class GoodHash(str):
    def __hash__(self) -> int:
        return ord(self[1]) + 26 * ord(self[0]) - 2619

baddict = set()
gooddict = set()
for i, j in zip(ascii_lowercase, ascii_lowercase):
    key = i + j
    baddict.add(BadHash(key))
    gooddict.add(GoodHash(key))

start = time()
for i in range(10**7):
    BadHash('tt')
print(f'BadHash: {round(time() - start, 2)} sec')
start = time()
for i in range(10**7):
    GoodHash('tt')
print(f'GoodHash: {round(time() - start, 2)} sec')