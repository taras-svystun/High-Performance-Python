def random_function():
    from guppy import hpy
    heap = hpy()
    print(heap.heap())
    lst = list()
    for i in range(10 ** 3):
        lst.append(i)
    print()
    print(heap.heap())
    for i in range(10 ** 3):
        lst.remove(i)
    print()
    print(heap.heap())

if __name__ == '__main__':
    random_function()