def random_function(spread=10 ** 6):
    counter = 0
    for i in range(spread):
        if abs(i) % 2:
            counter -= i ** 2
        if not i % 2:
            counter += 1
    return counter


if __name__ == '__main__':
    from line_profiler import LineProfiler

    profile = LineProfiler()
    lp_wrapper = profile(random_function)
    lp_wrapper()
    profile.print_stats()