---
title: fibonacci
tags: list
---


```python
def fibonacci(n):
    if n <= 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib


r = fibonacci(0)  # [1]
print(r)

r = fibonacci(5)  # [1, 1, 2, 3, 5]
print(r)
```