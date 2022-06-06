# In the terminal:
# python -m memory_profiler testing_code/2/memory_profiler_example.py
# Then to visuzalize:
# mprof plot mprofile_20220524161213.dat

@profile
def random_function(spread=10 ** 2):
    counter = 0
    lst = [[i for i in range(10 ** 2)] for j in range(10 ** 3)]
    lst1 = []
    lst2 = []
    for i in range(spread):
        if abs(i) % 2:
            for _ in range(10 ** 3):
                lst1.append(i)
        if not i % 2:
            for _ in range(10 ** 3):
                lst2.append(i)
    return counter

if __name__ == '__main__':
    random_function()