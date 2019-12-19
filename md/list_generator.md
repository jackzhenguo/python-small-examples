### 1 列表生成式和生成器

```python
from numpy import random
a = random.random(10000)

lst = []
for i in a:
    lst.append(i * i)  # 不推荐做法

lst = [i * i for i in a]  # 使用列表生成式

gen = (i * i for i in a)  # 生成器更节省内存
```

### 2 字典推导式创建子集
```python
a = {'apple': 5.6, 'orange': 4.7, 'banana': 2.8}
da = {key: value for key, value in a.items() if value > 4.0}
print(da)  # {'apple': 5.6, 'orange': 4.7}
```

### 3 使用itemgetter多字段排序
```python
from operator import itemgetter
a = [{'date': '2019-12-15', 'weather': 'cloud'},
     {'date': '2019-12-13', 'weather': 'sunny'},
     {'date': '2019-12-14', 'weather': 'cloud'}]

a.sort(key=itemgetter('weather', 'date'))
print(a)
# [{'date': '2019-12-14', 'weather': 'cloud'}, {'date': '2019-12-15', 'weather': 'cloud'}, {'date': '2019-12-13', 'weather': 'sunny'}]
```

### 4 使用itemgetter分组
```python
from operator import itemgetter
from itertools import groupby
a.sort(key=itemgetter('weather', 'date'))  # 必须先排序再分组
for k, items in groupby(a, key=itemgetter('weather')):
    print(k)
    for i in items:
        print(i)
```
### 5 sum类聚合函数与生成器

Python中的聚合类函数`sum`,`min`,`max`第一个参数是`iterable`类型，一般使用方法如下：
```python
a = [4,2,5,1]
sum([i+1 for i in a]) # 16
```
使用列表生成式`[i+1 for i in a]`创建一个长度与`a`一样的临时列表，这步完成后，再做`sum`聚合。

试想如果你的数组`a`长度是百万级，再创建一个这样的临时列表就很不划算，最好是一边算一边聚合，稍改动为如下：
```python
a = [4,2,5,1]
sum(i+1 for i in a) # 16
```
此时`i+1 for i in a`是`(i+1 for i in a)`的简写，得到一个生成器(`generator`)对象，如下所示：
```python
In [8]:(i+1 for i in a)
OUT [8]:<generator object <genexpr> at 0x000002AC7FFA8CF0>
```
生成器每迭代一步吐出(`yield`)一个元素并计算和聚合后，进入下一次迭代，直到终点。

### 6 ChainMap逻辑上合并多个字典
```python
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged = {**dic1, **dic2} # {'x': 1, 'y': 3, 'z': 4}
```
修改`merged['x']=10`，dic1中的`x`值`不变`

`ChainMap` 只在`逻辑上`合并，在内部创建了一个容纳这些字典的列表。
```python

from collections import ChainMap
merged = ChainMap(dic1,dic2)
print(merged)
# ChainMap({'x': 1, 'y': 2}, {'y': 3, 'z': 4})
```
使用`ChainMap`合并字典，修改`merged['x']=10`，dic1中的`x`值`改变`

### 7 namedtuple让代码更易维护
