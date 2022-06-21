from numpy.random import uniform
from time import time

def get_in_circle(n_iter: int):
    in_circle = 0
    for _ in range(n_iter):
        x, y = uniform(size=2)
        in_circle += x**2 + y **2 <= 1
    return in_circle

def estimate_pi(n_iter: int = 10 ** 6):
    return 4 * get_in_circle(n_iter) / n_iter
    

if __name__ == '__main__':
    start = time()
    print(estimate_pi())
    print(f'Naive method took: {round(time() - start, 2)} seconds')
