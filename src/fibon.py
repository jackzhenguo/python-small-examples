def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# for x in fibonacci(5):
#     print(x)
list(fibonacci(5))  # [1, 1, 2, 3, 5]

