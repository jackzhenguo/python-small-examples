### Python 小例子

#### 关于此库

Python小例子、小Demo一网打尽。Python基础、Web开发、数据科学、机器学习、TensorFlow、Pytorch，你能想到的基于Python的小Demo都在这里。

#### 欢迎贡献

比如github账号为`lhxon`的小伙伴，fork此库后，按照如下步骤贡献：
```markdown
1. git clone https://github.com/lhxon/python-small-examples
2. git add . 
3. git commit -m "xiugai"
4. git push
5. 界面点击：pull requests，根据操作即可。如遇问题，欢迎联系我。
```

#### 小例子列表
1. 交换两个元素
```python
def swap(a, b):
    return b, a
print(swap(1, 0))  # (0,1)
```

2. 求斐波那契数列前n项
```python
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
list(fibonacci(5))  # [1, 1, 2, 3, 5]
```

3. 返回更长列表
```python
def max_length(*lst):
    return max(*lst, key=lambda v: len(v))

max_length([1, 2, 3], [4, 5, 6, 7], [8]) # [4, 5, 6, 7]

```

4. 合并两个字典
```python
def merge_dict(dic1, dic2):
    return {**dic1, **dic2} 
    
merge_dict({'a': 1, 'b': 2}, {'c': 3})  # {'a': 1, 'b': 2, 'c': 3}
```

5. 列表反转
```python
def reverse(lst):
    return lst[::-1]
    
r = reverse([1, -2, 3, 4, 1, 2]) # [2, 1, 4, 3, -2, 1]
```

6. 等分list
```python
from math import ceil

def divide_iter(lst, n):
    if n <= 0:
        yield lst
        return
    i, div = 0, ceil(len(lst) / n)
    while i < n:
        yield lst[i * div: (i + 1) * div]
        i += 1

list(divide_iter([1, 2, 3, 4, 5], 0))  # [[1, 2, 3, 4, 5]]
list(divide_iter([1, 2, 3, 4, 5], 2))  # [[1, 2, 3], [4, 5]]
```
7. 查找指定后缀的文件
```python
import os

def find_file(work_dir,extension='jpg'):
    lst = []
    for filename in os.listdir(work_dir):
        print(filename)
        splits = os.path.splitext(filename)
        ext = splits[1] # 拿到扩展名
        if ext == '.'+extension:
            lst.append(filename)
    return lst

r = find_file('.','md')  # 返回所有目录下的md文件
```

8. 绘制漫天雪花

```python
import turtle as p
import random

def snow(snow_count):
    p.hideturtle()
    p.speed(500)
    p.pensize(2)
    for i in range(snow_count):
        r = random.random()
        g = random.random()
        b = random.random()
        p.pencolor(r, g, b)
        p.pu()
        p.goto(random.randint(-350, 350), random.randint(1, 270))
        p.pd()
        dens = random.randint(8, 12)
        snowsize = random.randint(10, 14)
        for _ in range(dens):
            p.forward(snowsize)  # 向当前画笔方向移动snowsize像素长度
            p.backward(snowsize)  # 向当前画笔相反方向移动snowsize像素长度
            p.right(360 / dens)  # 顺时针移动360 / dens度

def ground(ground_line_count):
    p.hideturtle()
    p.speed(500)
    for i in range(ground_line_count):
        p.pensize(random.randint(5, 10))
        x = random.randint(-400, 350)
        y = random.randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        p.pencolor(r, g, b)
        p.penup()  # 抬起画笔
        p.goto(x, y)  # 让画笔移动到此位置
        p.pendown()  # 放下画笔
        p.forward(random.randint(40, 100))  # 眼当前画笔方向向前移动40~100距离

def main():
    p.setup(800, 600, 0, 0)
    # p.tracer(False)
    p.bgcolor("black")
    snow(30)
    ground(30)
    # p.tracer(True)
    p.mainloop()

main()
```
结果：
![](./img/turtlesnow.gif)

9. 多列表最大值
```python 
def max_lists(*lst):
    return max(max(*lst, key=lambda v: max(v)))


max_lists([1, 2, 3], [6, 7, 8], [4, 5])# 8
```
10. 出现最多元素
```python
def max_frequency(lst):
    return max(lst, default='列表为空', key=lambda v: lst.count(v))


lst = [1, 3, 3, 2, 1, 1, 2]
r = max_frequency(lst)
print(f'{lst}中出现次数最多的元素为:{r}')  # [1, 3, 3, 2, 1, 1, 2]中出现次数最多的元素为:1
```
[更多小例子](./md/README.md)
















