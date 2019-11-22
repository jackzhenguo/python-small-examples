# 映射非可迭代对象为可迭代对象
from collections.abc import Iterable


def cast_iterable(val):
    return val if isinstance(val, Iterable) else [val]


print(cast_iterable('foo'))
print(cast_iterable(12))
print(cast_iterable({'foo': 12}))
# 结果
# foo
# [12]
# {'foo': 12}
