import numpy as np
from time import time

def numpy_get_in_circle(n_iter: int):
    np.random.seed()
    x, y = np.random.uniform(0, 1, n_iter), np.random.uniform(0, 1, n_iter)
    in_circle = x ** 2 + y ** 2 <= 1
    return np.sum(in_circle)

def estimate_pi(n_iter: int = 10 ** 6):
    return 4 * numpy_get_in_circle(n_iter) / n_iter
    
if __name__ == '__main__':
    start = time()
    print(estimate_pi())
    print(f'Numpy method took: {round(time() - start, 2)} seconds')
