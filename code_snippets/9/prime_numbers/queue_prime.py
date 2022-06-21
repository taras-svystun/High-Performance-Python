import math
import time
from multiprocessing import Pool, Manager, Process

ALL_DONE = "WORK_FINISHED"
WORKER_FINISHED_PROCESSING = "WORKER_FINISHED_PROCESSING"

def check_prime(possible_primes_queue, definite_primes_queue):
    while True:
        n = possible_primes_queue.get()
        if n == ALL_DONE:
            definite_primes_queue.put(WORKER_FINISHED_PROCESSING)
            break
        else:
            if n % 2 == 0:
                continue
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    break
            else:
                definite_primes_queue.put(n)


if __name__ == "__main__":
    primes = []
    manager = Manager()

    possible_primes_queue = manager.Queue()
    definite_primes_queue = manager.Queue()

    n_workers = 8
    pool = Pool(processes=n_workers)
    processes = []
    for _ in range(n_workers):
        p = Process(
            target=check_prime,
            args=(
                possible_primes_queue,
                definite_primes_queue))
        processes.append(p)
        p.start()

    t1 = time.time()
    number_range = range(10 ** 7, 10 ** 7 + 10 ** 5)  

    for possible_prime in number_range:
        possible_primes_queue.put(possible_prime)
    print("ALL JOBS ADDED TO THE QUEUE")

    # add poison pills to stop the remote workers
    for n in range(n_workers):
        possible_primes_queue.put(ALL_DONE)

    print("NOW WAITING FOR RESULTS...")
    processors_indicating_they_have_finished = 0
    while True:
        # block whilst waiting for results
        new_result = definite_primes_queue.get()
        if new_result == WORKER_FINISHED_PROCESSING:
            print(f"WORKER {processors_indicating_they_have_finished} HAS JUST FINISHED")
            processors_indicating_they_have_finished += 1
            if processors_indicating_they_have_finished == n_workers:
                break
        else:
            primes.append(new_result)
    assert processors_indicating_they_have_finished == n_workers

    print("Took:", time.time() - t1)
    print(len(primes), primes[:10], primes[-10:])