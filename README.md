### Python 小例子

告别枯燥，60秒学会一个Python小例子。Python基础、Web开发、数据科学、机器学习的精简小例子都在这里。

#### 欢迎贡献

比如github账号为`lhxon`的小伙伴，fork此库后，按照如下步骤提交到此库：

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
    
swap(1, 0)  # (0,1)
```
2. 反转list
```python
def reverse(lst):
    return lst[::-1]
    
reverse([1,2,3]) # [3,2,1]
```
3. 重复判断
```python
def duplicated(lst):
    return len(set(lst))!=len(lst)
    
duplicated([1,2,2,3]) # True:有重复
```
4. 次数最多
```python
def top1(lst):
    return max(lst, default='列表为空', key=lambda v: lst.count(v))
    
top1([1,2,3,3]) # 3
```
5. 更长列表
```python
def longer(*lst):
    return max(*lst, key=lambda v: len(v))
    
longer([1],[1,2],[1,2,3],[4,5]) #[1,2,3]
```
6. 表头
```python
def head(lst):
    return lst[0] if len(lst) > 0 else None
    
head([3,2,4,1,5]) # 3
```
7. 表尾
```python
def tail(lst):
    return lst[-1] if len(lst) > 0 else None

tail([3,2,4,1,5]) # 5
```
8. 元素对
```python
def pair(t):
    return list(zip(t[:-1],t[1:]))

pair([1,2,3]) # [(1, 2), (2, 3)]
```
9. 等分list

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
10. 多列表最大值

```python
def max_lists(*lst):
    return max(max(*lst, key=lambda v: max(v)))

max_lists([1, 2, 3], [6, 7, 8], [4, 5])# 8
```

11. 多列表最小值

```python
def min_lists(*lst):
    return min(min(*lst, key=lambda v: max(v)))

min_lists([1, 2, 3], [6, 7, 8], [4, 5])# 1 
```
12. 字典合并

```python
def merge(d1,d2):
    return {**d1,**d2}

merge({'a':1,'b':2},{'c':3}) # {'a': 1, 'b': 2, 'c': 3}
```
13. 合并差集

```python
def difference(d1,d2):
    return dict([(k,v) for k,v in d1.items() if k not in d2])

differece({'a':1,'b':2,'c':3},{'b':2}) # {'a': 1, 'c': 3}
```
14. 字典排序

```python
def sort_by_key(d):
    return sorted(d.items(),key=lambda x: x[0])

sort_by_key({'a':3,'b':1,'c':2}) # [('a', 3), ('b', 1), ('c', 2)]
```

15. 字符串的字节长

```python
def str_byte_len(mystr):
    return (len(mystr.encode('utf-8')))

str_byte_len('i love python')  # 13(个字节)
```

16. 求斐波那契数列前n项

```python
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
list(fibonacci(5))  # [1, 1, 2, 3, 5]
```

17. 查找指定后缀的文件

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

18. 打印99乘法表

```python
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(j,i,j*i),end="\t")
    print()
```

结果：

```markdown
1*1=1
1*2=2   2*2=4
1*3=3   2*3=6   3*3=9
1*4=4   2*4=8   3*4=12  4*4=16
1*5=5   2*5=10  3*5=15  4*5=20  5*5=25
1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36
1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49
1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64
1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
```

20. 绘制雪花

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
def main():
    p.setup(800, 600, 0, 0)
    p.bgcolor("black")
    snow(30)
    p.mainloop()

main()

```
<!-- ![漫天雪花](./img/turtlesnow.gif) -->
<img src="https://github.com/jackzhenguo/python-small-examples/blob/master/img/turtlesnow.gif" width="300" height="200" alt="图片名称" align=center>

[更多小例子](./md/README.md)
















