---
title: 求斐波那契数列前n项，生成器版本
tags: generator
---

```python
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


list(fibonacci(5))  # [1, 1, 2, 3, 5]
```
