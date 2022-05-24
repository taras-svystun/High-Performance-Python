from time import time

def time_decorator(func):
    def inner(*args, **kwargs):
        started = time()
        result = func(*args, **kwargs)
        elapsed_time = round(time() - started, 3)
        output = f'{func.__name__} took {elapsed_time} seconds.'
        print(output)
        return result
    return inner

@time_decorator
def random_function(spread):
    counter = 0
    for i in range(spread):
        if i % 2:
            counter -= 1
        if not i % 2:
            counter += 1
    return counter

if __name__ == '__main__':
    counter = random_function(10 ** 6)