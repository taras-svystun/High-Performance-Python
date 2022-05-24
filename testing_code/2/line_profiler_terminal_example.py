# In terminal write:
# kernprof -l testing_code/2/line_profiler_example.py
# python -m line_profiler line_profiler_example.py.lprof
# or
# kernprof -l -v testing_code/2/line_profiler_terminal_example.py

@profile
def random_function(spread=10 ** 6):
    counter = 0
    for i in range(spread):
        if abs(i) % 2:
            counter -= i ** 2
        if not i % 2:
            counter += 1
    return counter

if __name__ == '__main__':
    random_function(10 ** 6)