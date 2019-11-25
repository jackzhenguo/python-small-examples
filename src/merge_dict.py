from collections.abc import Iterable


def merge_dict(dic1, dic2):
    c = dic1.copy()
    c.update(dic2)
    return c


def merge_dict2(dic1, dic2):
    return {**dic1, **dic2}


r = merge_dict({'a': 1, 'b': 2}, {'c': 3})
print(r)

r = merge_dict2({'a': 1, 'b': 2}, {'c': 3})
print(r)


def transpose(lst):
    if len(lst) > 0 and isinstance(lst[0], Iterable) is False:
        return lst
    return list(map(lambda x: list(x), zip(*lst)))


# r = transpose([1, 2, 3])
# print(r)

r = transpose([[[1, 2, 3], [4, 5, 6]]])
print(r)
