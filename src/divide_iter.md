---
title: list分组的生成器实现方法
tags: generator,list
---

```python
from math import ceil


def divide_iter(lst, n):
    i, div = 0, ceil(len(lst) / n)
    while i < n:
        yield lst[i * div: (i + 1) * div]
        i += 1


list(divide_iter([1, 2, 3, 4, 5], 2))  # [[1, 2, 3], [4, 5]]
```