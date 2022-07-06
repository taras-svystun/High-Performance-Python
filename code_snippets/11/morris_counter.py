from multiprocessing import Pool
from time import perf_counter
import numpy as np
from numpy.random import uniform

import warnings
warnings.filterwarnings("ignore")

class MorrisCounter:
    def __init__(self):
        self.counter = 0

    def add(self, *args):
        if uniform() <= 2 ** -self.counter:
            self.counter += 1

    def __len__(self):
        return 2 ** self.counter

def run_experiment(*args):
    max_number = 2 * 10 ** 4
    counter = MorrisCounter()
    errors = np.zeros(max_number)

    for j in range(1, max_number):
        counter.add()
        errors[j] = (j - len(counter)) ** 2

    return errors[1:].mean()
    

if __name__ == '__main__':
    pool = Pool()
    n_exper = 10000
    start = perf_counter()

    means = pool.map(run_experiment, range(n_exper))

    mean, std = round(np.mean(means), 3), round(np.std(means), 3)
    print(f'Elapsed time: {round(perf_counter() - start, 2)}')
    print(f'Mean: {mean}, std: {std}, num of experiments: {n_exper}')
