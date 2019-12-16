今日分享

groupby分组

天气记录：
```python
a = [{'date': '2019-12-15', 'weather': 'cloud'},
 {'date': '2019-12-13', 'weather': 'sunny'},
 {'date': '2019-12-14', 'weather': 'cloud'}]
```
按照天气字段`weather`分组汇总：
```python
from itertools import groupby

for k, items in  groupby(a,key=lambda x:x['weather']):
	print(k)
```
输出结果看出，分组失败！原因：分组前必须按照分组字段`排序`，这个很坑~
```python
cloud
sunny
cloud
```
修改代码：
```python
a.sort(key=lambda x: x['weather'])
for k, items in  groupby(a,key=lambda x:x['weather']):
    print(k)
    for i in items:
        print(i)
```
输出结果：
```python
cloud
{'date': '2019-12-15', 'weather': 'cloud'}
{'date': '2019-12-14', 'weather': 'cloud'}
sunny
{'date': '2019-12-13', 'weather': 'sunny'}
```

注意到`sort`和`groupby`所用的`key`函数，除了`lambda`写法外，还有一种简写，就是使用`itemgetter`：

```python
a = [{'date': '2019-12-15', 'weather': 'cloud'},
 {'date': '2019-12-13', 'weather': 'sunny'},
 {'date': '2019-12-14', 'weather': 'cloud'}]
 
from operator import itemgetter
from itertools import groupby
a.sort(key=itemgetter('weather'))
for k, items in groupby(a, key=itemgetter('weather')):
    print(k)
    for i in items:
        print(i)
```
结果：
```python
cloud
{'date': '2019-12-15', 'weather': 'cloud'}
{'date': '2019-12-14', 'weather': 'cloud'}
sunny
{'date': '2019-12-13', 'weather': 'sunny'}
```

`itemgetter`是一个类，`itemgetter('weather')`返回一个可调用的对象，它的参数可有多个：
```python
from operator import itemgetter
from itertools import groupby
a.sort(key=itemgetter('weather', 'date'))
for k, items in groupby(a, key=itemgetter('weather')):
    print(k)
    for i in items:
        print(i)
```
结果如下，使用`weather`和`date`两个字段排序`a`，
```python
cloud
{'date': '2019-12-14', 'weather': 'cloud'}
{'date': '2019-12-15', 'weather': 'cloud'}
sunny
{'date': '2019-12-13', 'weather': 'sunny'}
```
注意这个结果与上面结果有些微妙不同，这个更多是我们想看到和使用更多的。