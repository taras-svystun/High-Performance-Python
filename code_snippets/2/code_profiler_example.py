# More info at
# https://docs.python.org/3/library/profile.html

if __name__ == '__main__':
    import cProfile
    import pstats

    def random_function(spread):
        counter = 0
        for i in range(spread):
            if abs(i) % 2:
                counter -= i ** 2
            if not i % 2:
                counter += 1
        return counter

    cProfile.run('random_function(10 ** 7)',
    'testing_code/2/code_profiler_example.stats', 'cumulative')

    p = pstats.Stats('testing_code/2/code_profiler_example.stats')
    p.sort_stats('cumulative')
    p.print_stats()
    p.print_callers()
    p.print_callees()