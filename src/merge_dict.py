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



