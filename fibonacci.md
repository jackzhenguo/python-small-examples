---
fibonacci序列：[0, 1, 1, 2, 3, 5, 8, ...]
---

```python
def fibonacci(n):
    if n <= 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib


r = fibonacci(0)
print(r)

r = fibonacci(5)
print(r)

# [0]
# [0, 1, 1, 2, 3]
