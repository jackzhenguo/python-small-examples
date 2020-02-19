from collections.abc import Iterable


def transpose(lst):
    if len(lst) > 0 and isinstance(lst[0], Iterable) is False:
        return lst
    return list(map(lambda x: list(x), zip(*lst)))


# r = transpose([1, 2, 3])
# print(r)

r = transpose([[1, 2, 3], [4, 5, 6]])
print(r)
