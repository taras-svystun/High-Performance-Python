import mmh3
from sortedcontainers import SortedSet


class KMinValues:

    def __init__(self, num_hashes):
        self.num_hashes = num_hashes
        self.data = SortedSet()

    def add(self, item):
        item_hash = mmh3.hash(item)
        self.data.add(item_hash)
        if len(self.data) > self.num_hashes:
            self.data.pop()

    def __len__(self):
        if len(self.data) <= 2:
            return 0
        print((self.num_hashes - 1) * (2 ** 32 - 1) /
              self.data[-2] + 2 ** 31 - 1)
        return int((self.num_hashes - 1) * (2 ** 32 - 1) /
                   (self.data[-2] + 2 ** 31 - 1))


if __name__ == '__main__':
    kminvalue1 = KMinValues(1024)
    kminvalue2 = KMinValues(1024)
    for i in range(50 * 10 ** 3):
        kminvalue1.add(str(i))
    for i in range(25 * 10 ** 3, 75 * 10 ** 3):
        kminvalue2.add(str(i))

    print(f'Length of kminvalue1: {len(kminvalue1)}')
    print(f'Length of kminvalue2: {len(kminvalue2)}')
    