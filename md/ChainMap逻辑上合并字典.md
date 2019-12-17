**ChainMap逻辑上合并多个字典**

1 两种合并字典方法
这是一般的字典合并写法
```python
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged1 = {**dic1, **dic2} # {'x': 1, 'y': 3, 'z': 4}
```

修改merged['x']=10，dic1中的x值`不变`，`merged`是重新生成的一个`新字典`。

但是，`ChainMap`却不同，它在内部创建了一个容纳这些字典的列表。因此使用ChainMap合并字典，修改merged['x']=10后，dic1中的x值`改变`，如下所示：

```python
from collections import ChainMap
merged2 = ChainMap(dic1,dic2)
print(merged2) # ChainMap({'x': 1, 'y': 2}, {'y': 3, 'z': 4})
```

2 ChainMap节省内存

`ChainMap`这种只在逻辑上合并字典的方法，可以大大节省内存的使用。普通的合并字典会重新创建一个字典，其占用内存会很大，演示如下：
```python
import sys
sys.getsizeof(merged1) # 240
```

结果显示会占用`240`个字节，`ChainMap`合并后的字典由于只是创建列表，其元素只是指针变量（指向了原来的字典），占用字节自然会小很多：
```python
sys.getsizeof(merged2) #56
```
只占用`56`个字节，相比第一种合并方法节省内存4倍多。