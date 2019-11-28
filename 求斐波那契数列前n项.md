

```python
# 求斐波那契数列前n项
#1、用生成器函数，减小运算占用内存
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        yield a
        a, b = b, a + b
    return result
for x in fibon(10):
    print(x)
#2、一般方法
def fibon(n):
    if n<=1:
        return [0]
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
fibon(10)
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    




    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


