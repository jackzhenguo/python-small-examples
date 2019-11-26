

def divide_iter(lst, n):
    i, div = 0, len(lst) // n
    while i < n:
        yield lst[i * div: (i + 1) * div]
        i += 1


list(divide_iter([1, 2, 3, 4, 5], 2))  # [[1, 2, 3], [4, 5]]
