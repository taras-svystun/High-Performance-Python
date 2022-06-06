def slow(upper=10**7):
    total = 0
    for i in range(upper):
        total += i
    return total

def fast(upper=10**7):
    return sum(range(upper))

if __name__ == '__main__':
    import dis
    from time import time
    start = time()
    # print(slow(), time() - start)
    start = time()
    # print(fast(), time() - start)
    dis.dis(slow)
    dis.dis(fast)