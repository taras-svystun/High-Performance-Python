from regular_python import get_in_circle
from numpy_implementation import numpy_get_in_circle
from time import time, sleep
from multiprocessing import Pool
import plotly.express as px

def estimate_pi(n_iter: int = 10**7, n_workers: int = 4):
    pool = Pool(processes=n_workers)
    samples_per_worker = int(n_iter / n_workers)
    n_iter_per_process = [samples_per_worker] * n_workers
    in_circle = pool.map(numpy_get_in_circle, n_iter_per_process)
    return 4 * sum(in_circle) / n_iter


if __name__ == '__main__':
    n_workers = [1, 2, 4, 8, 16]
    times = []
    for i in n_workers:
        start = time()
        estimate_pi(n_workers=i)
        times.append(round(time() - start, 2))
        sleep(2)
    print(times)
    fig = px.line(x=n_workers, y=times)
    fig.show()
        
