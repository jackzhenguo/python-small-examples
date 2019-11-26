def divide_iter(lst, n):
    i, div = 0, len(lst) // n
    while i < n:
        yield lst[i * div: (i + 1) * div]
        i += 1


list(divide_iter([1, 2, 3, 4, 5], 2))  # [[1, 2, 3], [4, 5]]


def divide(lst, size=2):
    from itertools import islice
    if size <= 0:
        yield list(lst)
    i, div = 0, len(lst) // size
    while i < size:
        yield list(islice(lst, i*div, (i + 1)*div))
        i += 1


print(list(divide([1, 2, 3, 4, 5], 2)))  # [[1, 2, 3], [4, 5]]
