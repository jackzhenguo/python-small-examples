---
title: 求字典前n个最大值
tags: dict,heapq,nlargest
---

```python
from heapq import nlargest

# 返回字典d前n个最大值对应的键


def topn_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])


topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3)  # ['a', 'd', 'c']
```