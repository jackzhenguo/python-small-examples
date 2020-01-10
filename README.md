告别枯燥，60秒学会一个小例子，系统学习Python，从入门到大师。**Python之路**已有`200`个例子：

引言：感受Python之美

第一章：Python基础 

第二章：Python之坑

第三章：Python字符串和正则

第四章：Python文件

第五章：Python日期

第六章：Python利器

第七章：Python画图

第八章：Python实用工具

第九章：Python实战

第十章：Python基础算法

第十一章：Python机器学习

> 后续章节：
>
> 1) 不断丰富原有1~7章节
> 2) PyQt制作GUI
> 3) Flask前端开发
> 4) Python数据分析


已发[《Python之路.1.2.pdf》](https://github.com/jackzhenguo/python-small-examples/releases/tag/V1.2.378)最新版本`V1.2.378`包括`11`个章节：`Python基础`，`Python之坑`,`Python字符串和正则`，`Python文件`，`Python日期`, `Python利器`，`Python画图` ,`Python实用工具`，`Python实战`, `Python基础算法`，`机器学习核心知识` 章节，目前超过`200个`小例子。

### 感受Python之美

#### 1 简洁之美

通过一行代码，体会Python语言简洁之美

1) 一行代码交换`a`,`b`：

```python
a, b = b, a
```

2) 一行代码反转列表

```python
[1,2,3][::-1] # [3,2,1]
```

3) 一行代码合并两个字典

```python
{**{'a':1,'b':2}, **{'c':3}} # {'a': 1, 'b': 2, 'c': 3}

```
4)  一行代码列表去重

```python
set([1,2,2,3,3,3]) # {1, 2, 3}
```

5) 一行代码求多个列表中的最大值

```python
max(max([ [1,2,3], [5,1], [4] ], key=lambda v: max(v))) # 5
```

6) 一行代码生成逆序序列

```python
list(range(10,-1,-1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### 2 Python绘图

Python绘图方便、漂亮，画图神器pyecharts几行代码就能绘制出热力图：

<img src="./img/image-20191229101724665.png" alt="Sample"  width="600" height="300">

炫酷的水球图：

<img src="./img/liquid.gif" alt="Sample"  width="600" height="450">

经常使用的词云图：

<img src="https://i.loli.net/2019/12/28/nSs8MY9Dc4I1egk.png" alt="Sample"  width="600" height="300">

#### 3 Python动画

仅适用Python的常用绘图库：Matplotlib，就能制作出动画，辅助算法新手入门基本的排序算法。如下为一个随机序列，使用`快速排序算法`，由小到大排序的过程动画展示：

<img src="https://mmbiz.qpic.cn/mmbiz_gif/FQd8gQcyN256Z0UkwIAVsP1pMsIUYTaHibX8xewf1Sgyvfh3VAR7IkWdwQtbNsniaiaXHzjG0Tcefl3Dv4OibhbGeg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1" alt="Sample"  width="600" height="300">

归并排序动画展示：

<img src="https://mmbiz.qpic.cn/mmbiz_gif/FQd8gQcyN256Z0UkwIAVsP1pMsIUYTaHpD5ibgM0kmia30zVM163X3RF9HnX2icibkJNghcibfjicxbibIJLLYprxqOqw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1" alt="Sample"  width="600" height="300">

使用turtule绘制的漫天雪花：

<img src="./img/turtlesnow.gif" alt="Sample"  width="600" height="300">

timeline时间轮播图：

<img src="./img/timeline.gif" alt="Sample"  width="600" height="300">

#### 4 Python数据分析

Python非常适合做数值计算、数据分析，一行代码完成数据透视：

```python
pd.pivot_table(df, index=['Manager', 'Rep'], values=['Price'], aggfunc=np.sum)
```

#### 5 Python机器学习

Python机器学习库`Sklearn`功能强大，接口易用，包括数据预处理模块、回归、分类、聚类、降维等。一行代码创建一个KMeans聚类模型：

```python
from sklearn.cluster import KMeans
KMeans( n_clusters=3 )
```

![img](https://mmbiz.qpic.cn/mmbiz_png/e4kxNicDVcCGpkBThJSo6hrL3NpV3iasxOXslKOpDkxqVApeZughwf6hRNCP8WBf7fGHfxUQiaFA4Z7HQexyHB2oA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 6 Python-GUI

PyQt设计器开发GUI，能够迅速通过拖动组建搭建出来，使用方便。如下为使用PyQt，定制的一个专属自己的小而美的计算器。

除此之外，使用Python的Flask框架搭建Web框架，也非常方便。

总之，在这个`Python小例子`，你都能学到关于使用Python干活的方方面面的有趣的小例子，欢迎关注。

### 一、Python基础

`Python基础`主要总结Python常用内置函数；Python独有的语法特性、关键词`nonlocal`, ` global`等；内置数据结构包括：列表(list),  字典(dict),  集合(set),  元组(tuple) 以及相关的高级模块`collections`中的`Counter`,  `namedtuple`, `defaultdict`，`heapq`模块。目前共有`86`个小例子。

#### 1 求绝对值

绝对值或复数的模

```python
In [1]: abs(-6)
Out[1]: 6
```

#### 2 元素都为真

接受一个迭代器，如果迭代器的`所有元素`都为真，那么返回`True`，否则返回`False`

```python
In [2]: all([1,0,3,6])
Out[2]: False

In [3]: all([1,2,3])
Out[3]: True
```

#### 3 元素至少一个为真　

接受一个迭代器，如果迭代器里`至少有一个`元素为真，那么返回`True`，否则返回`False`

```python
In [4]: any([0,0,0,[]])
Out[4]: False

In [5]: any([0,0,1])
Out[5]: True
```

#### 4 ascii展示对象　　

调用对象的__repr__() 方法，获得该方法的返回值，如下例子返回值为字符串

```python
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name
   ...: 
   ...: 

In [2]: xiaoming = Student(id='001',name='xiaoming')

In [3]: print(xiaoming)
id = 001, name = xiaoming

In [4]: ascii(xiaoming)
Out[4]: 'id = 001, name = xiaoming'
```

#### 5  十转二

将`十进制`转换为`二进制`

```python
In [1]: bin(10)
Out[1]: '0b1010'
```

#### 6 十转八

将`十进制`转换为`八进制`

```python
In [1]: oct(9)
Out[1]: '0o11'
```

#### 7 十转十六

将`十进制`转换为`十六进制`

```python
In [1]: hex(15)
Out[1]: '0xf'
```

#### 8 判断是真是假　　

测试一个对象是True, 还是False.

```python
In [1]: bool([0,0,0])
Out[1]: True

In [2]: bool([])
Out[2]: False

In [3]: bool([1,0,1])
Out[3]: True
```

#### 9  字符串转字节　　

将一个`字符串`转换成`字节`类型

```python
In [1]: s = "apple"

In [2]: bytes(s,encoding='utf-8')
Out[2]: b'apple'
```

#### 10 转为字符串　　

将`字符类型`、`数值类型`等转换为`字符串`类型

```python
In [1]: i = 100

In [2]: str(i)
Out[2]: '100'
```

#### 11 是否可调用　　

判断对象是否可被调用，能被调用的对象就是一个`callable` 对象，比如函数 `str`, `int` 等都是可被调用的，但是例子**4** 中`xiaoming`实例是不可被调用的：

```python
In [1]: callable(str)
Out[1]: True

In [2]: callable(int)
Out[2]: True

In [3]: xiaoming
Out[3]: id = 001, name = xiaoming

In [4]: callable(xiaoming)
Out[4]: False
```
如果想让`xiaoming`能被调用 xiaoming(), 需要重写`Student`类的`__call__`方法：

```python
In [1]: class Student():
    ...:     def __init__(self,id,name):
    ...:         self.id = id
    ...:         self.name = name
    ...:     def __repr__(self):
    ...:         return 'id = '+self.id +', name = '+self.name
    ...:     def __call__(self):
    ...:         print('I can be called')
    ...:         print(f'my name is {self.name}')
    ...: 
    ...: 

In [2]: t = Student('001','xiaoming')

In [3]: t()
I can be called
my name is xiaoming

```



#### 12 十转ASCII

查看十进制整数对应的`ASCII字符`

```python
In [1]: chr(65)
Out[1]: 'A'
```

#### 13 ASCII转十

查看某个`ASCII字符`对应的十进制数

```python
In [1]: ord('A')
Out[1]: 65
```

#### 14 静态方法　

`classmethod` 装饰器对应的函数不需要实例化，不需要 `self `参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。

```python
In [1]: class Student():
    ...:     def __init__(self,id,name):
    ...:         self.id = id
    ...:         self.name = name
    ...:     def __repr__(self):
    ...:         return 'id = '+self.id +', name = '+self.name
    ...:     @classmethod
    ...:     def f(cls):
    ...:         print(cls)
```

#### 15 执行字符串表示的代码

将字符串编译成python能识别或可执行的代码，也可以将文字读成字符串再编译。

```python
In [1]: s  = "print('helloworld')"
    
In [2]: r = compile(s,"<string>", "exec")
    
In [3]: r
Out[3]: <code object <module> at 0x0000000005DE75D0, file "<string>", line 1>
    
In [4]: exec(r)
helloworld
```

#### 16  创建复数

创建一个复数

```python
In [1]: complex(1,2)
Out[1]: (1+2j)
```

#### 17 动态删除属性　　

删除对象的属性

```python
In [1]: delattr(xiaoming,'id')

In [2]: hasattr(xiaoming,'id')
Out[2]: False
```

#### 18 转为字典　　

创建数据字典

```python
In [1]: dict()
Out[1]: {}

In [2]: dict(a='a',b='b')
Out[2]: {'a': 'a', 'b': 'b'}

In [3]: dict(zip(['a','b'],[1,2]))
Out[3]: {'a': 1, 'b': 2}

In [4]: dict([('a',1),('b',2)])
Out[4]: {'a': 1, 'b': 2}
```

#### 19 一键查看对象所有方法　

不带参数时返回`当前范围`内的变量、方法和定义的类型列表；带参数时返回`参数`的属性，方法列表。

```python
In [96]: dir(xiaoming)
Out[96]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 
 'name']
```

#### 20 取商和余数　　

分别取商和余数

```python
In [1]: divmod(10,3)
Out[1]: (3, 1)
```

#### 21 枚举对象　　

返回一个可以枚举的对象，该对象的next()方法将返回一个元组。

```python
In [1]: s = ["a","b","c"]
    ...: for i ,v in enumerate(s,1):
    ...:     print(i,v)
    ...:
1 a
2 b
3 c
```

#### 22 计算表达式

将字符串str 当成有效的表达式来求值并返回计算结果取出字符串中内容

```python
In [1]: s = "1 + 3 +5"
    ...: eval(s)
    ...:
Out[1]: 9
```

#### 23 查看变量所占字节数

```python
In [1]: import sys

In [2]: a = {'a':1,'b':2.0}

In [3]: sys.getsizeof(a) # 占用240个字节
Out[3]: 240
```

#### 24 过滤器　　

在函数中设定过滤条件，迭代元素，保留返回值为`True`的元素：

```python
In [1]: fil = filter(lambda x: x>10,[1,11,2,45,7,6,13])

In [2]: list(fil)
Out[2]: [11, 45, 13]
```

#### 25 转为浮点类型　

将一个整数或数值型字符串转换为浮点数

```python
In [1]: float(3)
Out[1]: 3.0
```
如果不能转化为浮点数，则会报`ValueError`:
```python
In [2]: float('a')
ValueError                                Traceback (most recent call last)
<ipython-input-11-99859da4e72c> in <module>()
----> 1 float('a')

ValueError: could not convert string to float: 'a'

```

#### 26 字符串格式化　

格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法。

```
In [104]: print("i am {0},age{1}".format("tom",18))
i am tom,age18
```

| 3.1415926  | {:.2f}  | 3.14      | 保留小数点后两位             |
| ---------- | ------- | --------- | ---------------------------- |
| 3.1415926  | {:+.2f} | +3.14     | 带符号保留小数点后两位       |
| -1         | {:+.2f} | -1.00     | 带符号保留小数点后两位       |
| 2.71828    | {:.0f}  | 3         | 不带小数                     |
| 5          | {:0>2d} | 05        | 数字补零 (填充左边, 宽度为2) |
| 5          | {:x<4d} | 5xxx      | 数字补x (填充右边, 宽度为4)  |
| 10         | {:x<4d} | 10xx      | 数字补x (填充右边, 宽度为4)  |
| 1000000    | {:,}    | 1,000,000 | 以逗号分隔的数字格式         |
| 0.25       | {:.2%}  | 25.00%    | 百分比格式                   |
| 1000000000 | {:.2e}  | 1.00e+09  | 指数记法                     |
| 18         | {:>10d} | ' 18'     | 右对齐 (默认, 宽度为10)      |
| 18         | {:<10d} | '18 '     | 左对齐 (宽度为10)            |
| 18         | {:^10d} | ' 18 '    | 中间对齐 (宽度为10)          |

#### 27 冻结集合　　

创建一个不可修改的集合。

```python
In [1]: frozenset([1,1,3,2,3])
Out[1]: frozenset({1, 2, 3})
```
因为不可修改，所以没有像`set`那样的`add`和`pop`方法

#### 28 动态获取对象属性　

获取对象的属性

```python
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name

In [2]: xiaoming = Student(id='001',name='xiaoming')
In [3]: getattr(xiaoming,'name') # 获取xiaoming这个实例的name属性值
Out[3]: 'xiaoming'
```

#### 29 对象是否有这个属性

```python
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name

In [2]: xiaoming = Student(id='001',name='xiaoming')
In [3]: hasattr(xiaoming,'name')
Out[3]: True

In [4]: hasattr(xiaoming,'address')
Out[4]: False
```

#### 30 返回对象的哈希值　　

返回对象的哈希值，值得注意的是自定义的实例都是可哈希的，`list`, `dict`, `set`等可变对象都是不可哈希的(unhashable)

  ```python
In [1]: hash(xiaoming)
Out[1]: 6139638

In [2]: hash([1,2,3])
TypeError                                 Traceback (most recent call last)
<ipython-input-32-fb5b1b1d9906> in <module>()
----> 1 hash([1,2,3])

TypeError: unhashable type: 'list'
  ```

#### 31  一键帮助　

返回对象的帮助文档

```python
In [1]: help(xiaoming)
Help on Student in module __main__ object:

class Student(builtins.object)
 |  Methods defined here:
 |
 |  __init__(self, id, name)
 |
 |  __repr__(self)
 |
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

#### 32 对象门牌号　

返回对象的内存地址

```python
In [1]: id(xiaoming)
Out[1]: 98234208
```

#### 33 获取用户输入　

获取用户输入内容

```python
In [1]: input()
aa
Out[1]: 'aa'
```

#### 34  转为整型　　

int(x, base =10) , x可能为字符串或数值，将x 转换为一个普通整数。如果参数是字符串，那么它可能包含符号和小数点。如果超出了普通整数的表示范围，一个长整数被返回。  

```python
In [1]: int('12',16)
Out[1]: 18
```

#### 35 isinstance

判断*object*是否为类*classinfo*的实例，是返回true

```python
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name

In [2]: xiaoming = Student(id='001',name='xiaoming')

In [3]: isinstance(xiaoming,Student)
Out[3]: True
```

#### 36 父子关系鉴定

```python
In [1]: class undergraduate(Student):
    ...:     def studyClass(self):
    ...:         pass
    ...:     def attendActivity(self):
    ...:         pass

In [2]: issubclass(undergraduate,Student)
Out[2]: True

In [3]: issubclass(object,Student)
Out[3]: False

In [4]: issubclass(Student,object)
Out[4]: True
```

如果class是classinfo元组中某个元素的子类，也会返回True

```python
In [1]: issubclass(int,(int,float))
Out[1]: True
```

#### 37 创建迭代器类型

使用`iter(obj, sentinel)`, 返回一个可迭代对象, sentinel可省略(一旦迭代到此元素，立即终止)

```python
In [1]: lst = [1,3,5]

In [2]: for i in iter(lst):
    ...:     print(i)
    ...:
1
3
5
```

```python
In [1]: class TestIter(object):
    ...:     def __init__(self):
    ...:         self.l=[1,3,2,3,4,5]
    ...:         self.i=iter(self.l)
    ...:     def __call__(self):  #定义了__call__方法的类的实例是可调用的
    ...:         item = next(self.i)
    ...:         print ("__call__ is called,fowhich would return",item)
    ...:         return item
    ...:     def __iter__(self): #支持迭代协议(即定义有__iter__()函数)
    ...:         print ("__iter__ is called!!")
    ...:         return iter(self.l)
In [2]: t = TestIter()
In [3]: t() # 因为实现了__call__，所以t实例能被调用
__call__ is called,which would return 1
Out[3]: 1

In [4]: for e in TestIter(): # 因为实现了__iter__方法，所以t能被迭代
    ...:     print(e)
    ...: 
__iter__ is called!!
1
3
2
3
4
5
```

#### 38 所有对象之根

object 是所有类的基类

```python
In [1]: o = object()

In [2]: type(o)
Out[2]: object
```

#### 39 打开文件

返回文件对象

```python
In [1]: fo = open('D:/a.txt',mode='r', encoding='utf-8')

In [2]: fo.read()
Out[2]: '\ufefflife is not so long,\nI use Python to play.'
```

mode取值表：

| 字符  | 意义                             |
| :---- | :------------------------------- |
| `'r'` | 读取（默认）                     |
| `'w'` | 写入，并先截断文件               |
| `'x'` | 排它性创建，如果文件已存在则失败 |
| `'a'` | 写入，如果文件存在则在末尾追加   |
| `'b'` | 二进制模式                       |
| `'t'` | 文本模式（默认）                 |
| `'+'` | 打开用于更新（读取与写入）       |

#### 40 次幂

base为底的exp次幂，如果mod给出，取余

```python
In [1]: pow(3, 2, 4)
Out[1]: 1
```

#### 41 打印

```python
In [5]: lst = [1,3,5]

In [6]: print(lst)
[1, 3, 5]

In [7]: print(f'lst: {lst}')
lst: [1, 3, 5]

In [8]: print('lst:{}'.format(lst))
lst:[1, 3, 5]

In [9]: print('lst:',lst)
lst: [1, 3, 5]
```



#### 42  创建属性的两种方式

返回 property 属性，典型的用法：

```python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    # 使用property类创建 property 属性
    x = property(getx, setx, delx, "I'm the 'x' property.")
```

使用python装饰器，实现与上完全一样的效果代码：

```python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```

#### 43 创建range序列

1) range(stop)
2) range(start, stop[,step])

生成一个不可变序列：

```python
In [1]: range(11)
Out[1]: range(0, 11)

In [2]: range(0,11,1)
Out[2]: range(0, 11)
```

#### 44 反向迭代器

```python
In [1]: rev = reversed([1,4,2,3,1])

In [2]: for i in rev:
     ...:     print(i)
     ...:
1
3
2
4
1
```

#### 45 四舍五入

四舍五入，`ndigits`代表小数点后保留几位：

```python
In [11]: round(10.0222222, 3)
Out[11]: 10.022

In [12]: round(10.05,1)
Out[12]: 10.1
```

#### 46 转为集合类型

返回一个set对象，集合内不允许有重复元素：

```python
In [159]: a = [1,4,2,3,1]

In [160]: set(a)
Out[160]: {1, 2, 3, 4}
```

#### 47 转为切片对象

*class* slice(*start*, *stop*[, *step*])

返回一个表示由 range(start, stop, step) 所指定索引集的 slice对象，它让代码可读性、可维护性变好。

```python
In [1]: a = [1,4,2,3,1]

In [2]: my_slice_meaning = slice(0,5,2)

In [3]: a[my_slice_meaning]
Out[3]: [1, 2, 1]
```

#### 48 拿来就用的排序函数

排序：

```python
In [1]: a = [1,4,2,3,1]

In [2]: sorted(a,reverse=True)
Out[2]: [4, 3, 2, 1, 1]

In [3]: a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'
     ...: xiaohong','age':20,'gender':'female'}]
In [4]: sorted(a,key=lambda x: x['age'],reverse=False)
Out[4]:
[{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
 {'name': 'xiaohong', 'age': 20, 'gender': 'female'}]
```

####49 求和函数

求和：

```python
In [181]: a = [1,4,2,3,1]

In [182]: sum(a)
Out[182]: 11

In [185]: sum(a,10) #求和的初始值为10
Out[185]: 21
```

#### 50 转元组

 `tuple()` 将对象转为一个不可变的序列类型

 ```python
 In [16]: i_am_list = [1,3,5]
 In [17]: i_am_tuple = tuple(i_am_list)
 In [18]: i_am_tuple
 Out[18]: (1, 3, 5)
 ```

#### 51 查看对象类型

*class* `type`(*name*, *bases*, *dict*)

传入一个参数时，返回 *object* 的类型：

```python
In [1]: class Student():
   ...:     def __init__(self,id,name):
   ...:         self.id = id
   ...:         self.name = name
   ...:     def __repr__(self):
   ...:         return 'id = '+self.id +', name = '+self.name
   ...: 
   ...: 

In [2]: xiaoming = Student(id='001',name='xiaoming')
In [3]: type(xiaoming)
Out[3]: __main__.Student

In [4]: type(tuple())
Out[4]: tuple
```

#### 52 聚合迭代器

创建一个聚合了来自每个可迭代对象中的元素的迭代器：

```python
In [1]: x = [3,2,1]
In [2]: y = [4,5,6]
In [3]: list(zip(y,x))
Out[3]: [(4, 3), (5, 2), (6, 1)]

In [4]: a = range(5)
In [5]: b = list('abcde')
In [6]: b
Out[6]: ['a', 'b', 'c', 'd', 'e']
In [7]: [str(y) + str(x) for x,y in zip(a,b)]
Out[7]: ['a0', 'b1', 'c2', 'd3', 'e4']
```

#### 53 nonlocal用于内嵌函数中

关键词`nonlocal`常用于函数嵌套中，声明变量`i`为非局部变量；
如果不声明，`i+=1`表明`i`为函数`wrapper`内的局部变量，因为在`i+=1`引用(reference)时,i未被声明，所以会报`unreferenced variable`的错误。
```python
def excepter(f):
    i = 0
    t1 = time.time()
    def wrapper(): 
        try:
            f()
        except Exception as e:
            nonlocal i
            i += 1
            print(f'{e.args[0]}: {i}')
            t2 = time.time()
            if i == n:
                print(f'spending time:{round(t2-t1,2)}')
    return wrapper
```

#### 54 global 声明全局变量
先回答为什么要有`global`，一个变量被多个函数引用，想让全局变量被所有函数共享。有的伙伴可能会想这还不简单，这样写：
```python
i = 5
def f():
    print(i)

def g():
    print(i)
    pass

f()
g()

```
f和g两个函数都能共享变量`i`，程序没有报错，所以他们依然不明白为什么要用`global`.

但是，如果我想要有个函数对`i`递增，这样：
```python
def h():
    i += 1

h()
```
此时执行程序，bang, 出错了！ 抛出异常：`UnboundLocalError`，原来编译器在解释`i+=1`时会把`i`解析为函数`h()`内的局部变量，很显然在此函数内，编译器找不到对变量`i`的定义，所以会报错。

`global`就是为解决此问题而被提出，在函数h内，显示地告诉编译器`i`为全局变量，然后编译器会在函数外面寻找`i`的定义，执行完`i+=1`后，`i`还为全局变量，值加1：
```python
i = 0
def h():
    global i
    i += 1

h()
print(i)
```

#### 55 链式比较

```python
i = 3
print(1 < i < 3)  # False
print(1 < i <= 3)  # True
```


#### 56 不用else和if实现计算器

```python
from operator import *


def calculator(a, b, k):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '**': pow
    }[k](a, b)


calculator(1, 2, '+')  # 3
calculator(3, 4, '**')  # 81
```

#### 57 链式操作

```python
from operator import (add, sub)


def add_or_sub(a, b, oper):
    return (add if oper == '+' else sub)(a, b)


add_or_sub(1, 2, '-')  # -1
```

#### 58 交换两元素

```python
def swap(a, b):
    return b, a


print(swap(1, 0))  # (0,1)
```

#### 59 去最求平均

```python
def score_mean(lst):
    lst.sort()
    lst2=lst[1:(len(lst)-1)]
    return round((sum(lst2)/len(lst2)),1)

lst=[9.1, 9.0,8.1, 9.7, 19,8.2, 8.6,9.8]
score_mean(lst) # 9.1
```

#### 60 打印99乘法表

打印出如下格式的乘法表

```python
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

一共有10 行，第`i`行的第`j`列等于：`j*i`，

其中,

 `i`取值范围：`1<=i<=9`

 `j`取值范围：`1<=j<=i`

根据`例子分析`的语言描述，转化为如下代码：

```python
for i in range(1,10):
    ...:     for j in range(1,i+1):
    ...:         print('%d*%d=%d'%(j,i,j*i),end="\t")
    ...:     print()
```

#### 61 全展开

对于如下数组：

```
[[[1,2,3],[4,5]]]
```

如何完全展开成一维的。这个小例子实现的`flatten`是递归版，两个参数分别表示带展开的数组，输出数组。

```python
from collections.abc import *

def flatten(lst, out_lst=None):
    if out_lst is None:
        out_lst = []
    for i in lst:
        if isinstance(i, Iterable): # 判断i是否可迭代
            flatten(i, out_lst)  # 尾数递归
        else:
            out_lst.append(i)    # 产生结果
    return out_lst
```

调用`flatten`:

```python
print(flatten([[1,2,3],[4,5]]))
print(flatten([[1,2,3],[4,5]], [6,7]))
print(flatten([[[1,2,3],[4,5,6]]]))
# 结果：
[1, 2, 3, 4, 5]
[6, 7, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
```

numpy里的`flatten`与上面的函数实现有些微妙的不同：

```python
import numpy
b = numpy.array([[1,2,3],[4,5]])
b.flatten()
array([list([1, 2, 3]), list([4, 5])], dtype=object)
```

#### 62 列表等分

```python
from math import ceil

def divide(lst, size):
    if size <= 0:
        return [lst]
    return [lst[i * size:(i+1)*size] for i in range(0, ceil(len(lst) / size))]


r = divide([1, 3, 5, 7, 9], 2)
print(r)  # [[1, 3], [5, 7], [9]]

r = divide([1, 3, 5, 7, 9], 0)
print(r)  # [[1, 3, 5, 7, 9]]

r = divide([1, 3, 5, 7, 9], -3)
print(r)  # [[1, 3, 5, 7, 9]]

```

#### 63 列表压缩

```python
def filter_false(lst):
    return list(filter(bool, lst))


r = filter_false([None, 0, False, '', [], 'ok', [1, 2]])
print(r)  # ['ok', [1, 2]]

```

#### 64 更长列表

```python
def max_length(*lst):
    return max(*lst, key=lambda v: len(v))


r = max_length([1, 2, 3], [4, 5, 6, 7], [8])
print(f'更长的列表是{r}')  # [4, 5, 6, 7]

r = max_length([1, 2, 3], [4, 5, 6, 7], [8, 9])
print(f'更长的列表是{r}')  # [4, 5, 6, 7]
```

#### 65 求众数

```python
def top1(lst):
    return max(lst, default='列表为空', key=lambda v: lst.count(v))

lst = [1, 3, 3, 2, 1, 1, 2]
r = top1(lst)
print(f'{lst}中出现次数最多的元素为:{r}')  # [1, 3, 3, 2, 1, 1, 2]中出现次数最多的元素为:1
```

#### 66 多表之最
```python 
def max_lists(*lst):
    return max(max(*lst, key=lambda v: max(v)))


r = max_lists([1, 2, 3], [6, 7, 8], [4, 5])
print(r)  # 8
```

#### 67 列表查重

```python
def has_duplicates(lst):
    return len(lst) == len(set(lst))


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # False
has_duplicates(y)  # True
```




#### 68 列表反转

```python
def reverse(lst):
    return lst[::-1]


r = reverse([1, -2, 3, 4, 1, 2])
print(r)  # [2, 1, 4, 3, -2, 1]
```

#### 69 浮点数等差数列

```python
def rang(start, stop, n):
    start,stop,n = float('%.2f' % start), float('%.2f' % stop),int('%.d' % n)
    step = (stop-start)/n
    lst = [start]
    while n > 0:
        start,n = start+step,n-1
        lst.append(round((start), 2))
    return lst

rang(1, 8, 10) # [1.0, 1.7, 2.4, 3.1, 3.8, 4.5, 5.2, 5.9, 6.6, 7.3, 8.0]
```

#### 70 按条件分组

```python
def bif_by(lst, f):
    return [ [x for x in lst if f(x)],[x for x in lst if not f(x)]]

records = [25,89,31,34] 
bif_by(records, lambda x: x<80) # [[25, 31, 34], [89]]
```


#### 71 map实现向量运算

```python
#多序列运算函数—map(function,iterabel,iterable2)
lst1=[1,2,3,4,5,6]
lst2=[3,4,5,6,3,2]
list(map(lambda x,y:x*y+1,lst1,lst2))
### [4, 9, 16, 25, 16, 13]
```

#### 72 值最大的字典

```python
def max_pairs(dic):
    if len(dic) == 0:
        return dic
    max_val = max(map(lambda v: v[1], dic.items()))
    return [item for item in dic.items() if item[1] == max_val]


r = max_pairs({'a': -10, 'b': 5, 'c': 3, 'd': 5})
print(r)  # [('b', 5), ('d', 5)]
```

#### 73 合并两个字典

```python
def merge_dict(dic1, dic2):
    return {**dic1, **dic2}  # python3.5后支持的一行代码实现合并字典

merge_dict({'a': 1, 'b': 2}, {'c': 3})  # {'a': 1, 'b': 2, 'c': 3}
```

#### 74 topn字典

```python
from heapq import nlargest

# 返回字典d前n个最大值对应的键

def topn_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])

topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3)  # ['a', 'd', 'c']
```


#### 75 异位词

```python
from collections import Counter

# 检查两个字符串是否 相同字母异序词，简称：互为变位词

def anagram(str1, str2):
    return Counter(str1) == Counter(str2)

anagram('eleven+two', 'twelve+one')  # True 这是一对神器的变位词
anagram('eleven', 'twelve')  # False
```


#### 76 逻辑上合并字典
(1) 两种合并字典方法
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

#### 77 命名元组提高可读性

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])  # 定义名字为Point的元祖，字段属性有x,y,z
lst = [Point(1.5, 2, 3.0), Point(-0.3, -1.0, 2.1), Point(1.3, 2.8, -2.5)]
print(lst[0].y - lst[1].y)
```

使用命名元组写出来的代码可读性更好，尤其处理上百上千个属性时作用更加凸显。

#### 78 样本抽样

使用`sample`抽样，如下例子从100个样本中随机抽样10个。

```python
from random import randint,sample
lst = [randint(0,50) for _ in range(100)]
print(lst[:5])# [38, 19, 11, 3, 6]
lst_sample = sample(lst,10)
print(lst_sample) # [33, 40, 35, 49, 24, 15, 48, 29, 37, 24]
```

#### 79 重洗数据集

使用`shuffle`用来重洗数据集，**值得注意`shuffle`是对lst就地(in place)洗牌，节省存储空间**

```python
from random import shuffle
lst = [randint(0,50) for _ in range(100)]
shuffle(lst)
print(lst[:5]) # [50, 3, 48, 1, 26]
```

#### 80 10个均匀分布的坐标点

random模块中的`uniform(a,b)`生成[a,b)内的一个随机数，如下生成10个均匀分布的二维坐标点

```python
from random import uniform
In [1]: [(uniform(0,10),uniform(0,10)) for _ in range(10)]
Out[1]: 
[(9.244361194237328, 7.684326645514235),
 (8.129267671737324, 9.988395854203773),
 (9.505278771040661, 2.8650440524834107),
 (3.84320100484284, 1.7687190176304601),
 (6.095385729409376, 2.377133802224657),
 (8.522913365698605, 3.2395995841267844),
 (8.827829601859406, 3.9298809217233766),
 (1.4749644859469302, 8.038753079253127),
 (9.005430657826324, 7.58011186920019),
 (8.700789540392917, 1.2217577293254112)]
```

#### 81 10个高斯分布的坐标点

random模块中的`gauss(u,sigma)`生成均值为u, 标准差为sigma的满足高斯分布的值，如下生成10个二维坐标点，样本误差(y-2*x-1)满足均值为0，标准差为1的高斯分布：

```python
from random import gauss
x = range(10)
y = [2*xi+1+gauss(0,1) for xi in x]
points = list(zip(x,y))
### 10个二维点：
[(0, -0.86789025305992),
 (1, 4.738439437453464),
 (2, 5.190278040856102),
 (3, 8.05270893133576),
 (4, 9.979481700775292),
 (5, 11.960781766216384),
 (6, 13.025427054303737),
 (7, 14.02384035204836),
 (8, 15.33755823101161),
 (9, 17.565074449028497)]
```

#### 82 chain高效串联多个容器对象

`chain`函数串联a和b，兼顾内存效率同时写法更加优雅。

```python
from itertools import chain
a = [1,3,5,0]
b = (2,4,6)

for i in chain(a,b):
  print(i)
### 结果
1
3
5
0
2
4
6
```

#### 83 操作函数对象

```python
In [31]: def f():
    ...:     print('i\'m f')
    ...:

In [32]: def g():
    ...:     print('i\'m g')
    ...:

In [33]: [f,g][1]()
i'm g
```

创建函数对象的list，根据想要调用的index，方便统一调用。

#### 84 生成逆序序列

```python
list(range(10,-1,-1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

第三个参数为负时，表示从第一个参数开始递减，终止到第二个参数(不包括此边界)

#### 85 函数的五类参数使用例子

python五类参数：位置参数，关键字参数，默认参数，可变位置或关键字参数的使用。

```python
def f(a,*b,c=10,**d):
  print(f'a:{a},b:{b},c:{c},d:{d}')
```
*默认参数`c`不能位于可变关键字参数`d`后.*

调用f:
```python
In [10]: f(1,2,5,width=10,height=20)
a:1,b:(2, 5),c:10,d:{'width': 10, 'height': 20}
```
可变位置参数`b`实参后被解析为元组`(2,5)`;而c取得默认值10; d被解析为字典.

再次调用f:
```python
In [11]: f(a=1,c=12)
a:1,b:(),c:12,d:{}
```
a=1传入时a就是关键字参数，b,d都未传值，c被传入12，而非默认值。

注意观察参数`a`, 既可以`f(1)`,也可以`f(a=1)` 其可读性比第一种更好，建议使用f(a=1)。如果要强制使用`f(a=1)`，需要在前面添加一个**星号**:
```python
def f(*,a,*b):
  print(f'a:{a},b:{b}')
```
此时f(1)调用，将会报错：`TypeError: f() takes 0 positional arguments but 1 was given`

只能`f(a=1)`才能OK.

说明前面的`*`发挥作用，它变为只能传入关键字参数，那么如何查看这个参数的类型呢？借助python的`inspect`模块：

```python
In [22]: for name,val in signature(f).parameters.items():
    ...:     print(name,val.kind)
    ...:
a KEYWORD_ONLY
b VAR_KEYWORD
```

可看到参数`a`的类型为`KEYWORD_ONLY`，也就是仅仅为关键字参数。

但是，如果f定义为：
```python
def f(a,*b):
  print(f'a:{a},b:{b}')
```
查看参数类型：
```python
In [24]: for name,val in signature(f).parameters.items():
    ...:     print(name,val.kind)
    ...:
a POSITIONAL_OR_KEYWORD
b VAR_POSITIONAL
```
可以看到参数`a`既可以是位置参数也可是关键字参数。

#### 86  使用slice对象

生成关于蛋糕的序列cake1：

```
In [1]: cake1 = list(range(5,0,-1))

In [2]: b = cake1[1:10:2]

In [3]: b
Out[3]: [4, 2]

In [4]: cake1
Out[4]: [5, 4, 3, 2, 1]
```

再生成一个序列：

```
In [5]: from random import randint
   ...: cake2 = [randint(1,100) for _ in range(100)]
   ...: # 同样以间隔为2切前10个元素，得到切片d
   ...: d = cake2[1:10:2]
In [6]: d
Out[6]: [75, 33, 63, 93, 15]
```

你看，我们使用同一种切法，分别切开两个蛋糕cake1,cake2. 后来发现这种切法`极为经典`，又拿它去切更多的容器对象。

那么，为什么不把这种切法封装为一个对象呢？于是就有了slice对象。

定义slice对象极为简单，如把上面的切法定义成slice对象：

```
perfect_cake_slice_way = slice(1,10,2)
#去切cake1
cake1_slice = cake1[perfect_cake_slice_way] 
cake2_slice = cake2[perfect_cake_slice_way]

In [11]: cake1_slice
Out[11]: [4, 2]

In [12]: cake2_slice
Out[12]: [75, 33, 63, 93, 15]
```

与上面的结果一致。

对于逆向序列切片，`slice`对象一样可行：

```
a = [1,3,5,7,9,0,3,5,7]
a_ = a[5:1:-1]

named_slice = slice(5,1,-1)
a_slice = a[named_slice] 

In [14]: a_
Out[14]: [0, 9, 7, 5]

In [15]: a_slice
Out[15]: [0, 9, 7, 5]
```

频繁使用同一切片的操作可使用slice对象抽出来，复用的同时还能提高代码可读性。

### 二 Python之坑

#### 1 含单个元素的元组

Python中有些函数的参数类型为元组，其内有1个元素，这样创建是错误的：

```python
c = (5) # NO!
```

它实际创建一个整型元素5，必须要在元素后加一个`逗号`:

```python
c = (5,) # YES!
```

#### 2 默认参数设为空

含有默认参数的函数，如果类型为容器，且设置为空：

```python
def f(a,b=[]):  # NO!
    print(b)
    return b

ret = f(1)
ret.append(1)
ret.append(2)
# 当再调用f(1)时，预计打印为 []
f(1)
# 但是却为 [1,2]
```

这是可变类型的默认参数之坑，请务必设置此类默认参数为None：

```python
def f(a,b=None): # YES!
    pass
```

#### 3 共享变量未绑定之坑

有时想要多个函数共享一个全局变量，但却在某个函数内试图修改它为局部变量：

```python
i = 1
def f():
    i+=1 #NO!
    
def g():
    print(i)
```

应该在f函数内显示声明`i`为global变量：

```python
i = 1
def f():
    global i # YES!
    i+=1
```

#### 4 lambda自由参数之坑

排序和分组的key函数常使用lambda，表达更加简洁，但是有个坑新手容易掉进去：

```python
a = [lambda x: x+i for i in range(3)] # NO!
for f in a:
    print(f(1))
# 你可能期望输出：1,2,3
```

但是实际却输出: 3,3,3. 定义lambda使用的`i`被称为自由参数，它只在调用lambda函数时，值才被真正确定下来，这就犹如下面打印出2，你肯定确信无疑吧。

```python
a = 0
a = 1
a = 2
def f(a):
    print(a)
```

正确做法是转化`自由参数`为lambda函数的`默认参数`：

```python
a = [lambda x,i=i: x+i for i in range(3)] # YES!
```

#### 5 各种参数使用之坑

Python强大多变，原因之一在于函数参数类型的多样化。方便的同时，也为使用者带来更多的约束规则。如果不了解这些规则，调用函数时，可能会出现如下一些语法异常：

*(1) SyntaxError: positional argument follows keyword argument*


*(2) TypeError: f() missing 1 required keyword-only argument: 'b'*


*(3) SyntaxError: keyword argument repeated*

*(4) TypeError: f() missing 1 required positional argument: 'b'*

*(5) TypeError: f() got an unexpected keyword argument 'a'*

*(6) TypeError: f() takes 0 positional arguments but 1 was given*


总结主要的参数使用规则

位置参数

`位置参数`的定义：`函数调用`时根据函数定义的参数位（形参）置来传递参数，是最常见的参数类型。

```python
def f(a):
  return a

f(1) # 位置参数 
```
位置参数不能缺少：
```python
def f(a,b):
  pass

f(1) # TypeError: f() missing 1 required positional argument: 'b'
```

**规则1：位置参数必须一一对应，缺一不可**

关键字参数

在函数调用时，通过‘键--值’方式为函数形参传值，不用按照位置为函数形参传值。

```python
def f(a):
  print(f'a:{a}')
```
这么调用，`a`就是关键字参数：
```python
f(a=1)
```
但是下面调用就不OK:
```python
f(a=1,20.) # SyntaxError: positional argument follows keyword argument
```

**规则2：关键字参数必须在位置参数右边**


下面调用也不OK:
```python
f(1,width=20.,width=30.) #SyntaxError: keyword argument repeated

```

**规则3：对同一个形参不能重复传值**


默认参数

在定义函数时，可以为形参提供默认值。对于有默认值的形参，调用函数时如果为该参数传值，则使用传入的值，否则使用默认值。如下`b`是默认参数：
```python
def f(a,b=1):
  print(f'a:{a}, b:{b}')

```


**规则4：无论是函数的定义还是调用，默认参数的定义应该在位置形参右面**

只在定义时赋值一次；默认参数通常应该定义成不可变类型


可变位置参数

如下定义的参数a为可变位置参数：
```python
def f(*a):
  print(a)
```
调用方法：
```python
f(1) #打印结果为元组： (1,)
f(1,2,3) #打印结果：(1, 2, 3)
```

但是，不能这么调用：
```python
f(a=1) # TypeError: f() got an unexpected keyword argument 'a'
```


可变关键字参数

如下`a`是可变关键字参数：
```python
def f(**a):
  print(a)
```
调用方法：
```python
f(a=1) #打印结果为字典：{'a': 1}
f(a=1,b=2,width=3) #打印结果：{'a': 1, 'b': 2, 'width': 3}
```

但是，不能这么调用：
```python
f(1) TypeError: f() takes 0 positional arguments but 1 was given
```

接下来，单独推送分析一个小例子，综合以上各种参数类型的函数及调用方法，敬请关注。

#### 6 列表删除之坑

删除一个列表中的元素，此元素可能在列表中重复多次：

```python
def del_item(lst,e):
    return [lst.remove(i) for i in e if i==e] # NO!
```

考虑删除这个序列[1,3,3,3,5]中的元素3，结果发现只删除其中两个：

```python
del_item([1,3,3,3,5],3) # 结果：[1,3,5]
```

正确做法：

```python
def del_item(lst,e):
    d = dict(zip(range(len(lst)),lst)) # YES! 构造字典
    return [v for k,v in d.items() if v!=e]

```

#### 7 列表快速复制之坑

在python中`*`与列表操作，实现快速元素复制：

```python
a = [1,3,5] * 3 # [1,3,5,1,3,5,1,3,5]
a[0] = 10 # [10, 2, 3, 1, 2, 3, 1, 2, 3]
```

如果列表元素为列表或字典等复合类型：

```python
a = [[1,3,5],[2,4]] * 3 # [[1, 3, 5], [2, 4], [1, 3, 5], [2, 4], [1, 3, 5], [2, 4]]

a[0][0] = 10 #  
```

结果可能出乎你的意料，其他`a[1[0]`等也被修改为10

```python
[[10, 3, 5], [2, 4], [10, 3, 5], [2, 4], [10, 3, 5], [2, 4]]
```

这是因为*复制的复合对象都是浅引用，也就是说id(a[0])与id(a[2])门牌号是相等的。如果想要实现深复制效果，这么做：

```python
a = [[] for _ in range(3)]
```

#### 8 字符串驻留
```python
In [1]: a = 'something'
    ...: b = 'some'+'thing'
    ...: id(a)==id(b)
Out[1]: True
```
如果上面例子返回`True`，但是下面例子为什么是`False`:
```python
In [1]: a = '@zglg.com'

In [2]: b = '@zglg'+'.com'

In [3]: id(a)==id(b)
Out[3]: False
```
这与Cpython 编译优化相关，行为称为`字符串驻留`，但驻留的字符串中只包含字母，数字或下划线。

#### 9 相同值的不可变对象
```python
In [5]: d = {}
    ...: d[1] = 'java'
    ...: d[1.0] = 'python'

In [6]: d
Out[6]: {1: 'python'}

### key=1,value=java的键值对神器消失了
In [7]: d[1]
Out[7]: 'python'
In [8]: d[1.0]
Out[8]: 'python'
```
这是因为具有相同值的不可变对象在Python中始终具有`相同的哈希值`

由于存在`哈希冲突`，不同值的对象也可能具有相同的哈希值。

#### 10 对象销毁顺序
创建一个类`SE`:
```python
class SE(object):
  def __init__(self):
    print('init')
  def __del__(self):
    print('del')
```
创建两个SE实例，使用`is`判断：
```python
In [63]: SE() is SE()
init
init
del
del
Out[63]: False

```
创建两个SE实例，使用`id`判断：
```python
In [64]: id(SE()) == id(SE())
init
del
init
del
Out[64]: True
```

调用`id`函数, Python 创建一个 SE 类的实例，并使用`id`函数获得内存地址后，销毁内存丢弃这个对象。

当连续两次进行此操作, Python会将相同的内存地址分配给第二个对象，所以两个对象的id值是相同的.


但是is行为却与之不同，通过打印顺序就可以看到。

#### 11 充分认识for
```python
In [65]: for i in range(5):
    ...:   print(i)
    ...:   i = 10
0
1
2
3
4
```
为什么不是执行一次就退出？

按照for在Python中的工作方式, i = 10 并不会影响循环。range(5)生成的下一个元素就被解包，并赋值给目标列表的变量`i`.

#### 12 认识执行时机

```python
array = [1, 3, 5]
g = (x for x in array if array.count(x) > 0)
```
`g`为生成器，list(g)后返回`[1,3,5]`，因为每个元素肯定至少都出现一次。所以这个结果这不足为奇。但是，请看下例：
```python
array = [1, 3, 5]
g = (x for x in array if array.count(x) > 0)
array = [5, 7, 9]
```
请问,list(g)等于多少？这不是和上面那个例子结果一样吗，结果也是`[1,3,5]`，但是：
```python
In [74]: list(g)
Out[74]: [5]
```

这有些不可思议~~ 原因在于：

生成器表达式中, in 子句在声明时执行, 而条件子句则是在运行时执行。


所以代码：
```python
array = [1, 3, 5]
g = (x for x in array if array.count(x) > 0)
array = [5, 7, 9]
```

等价于：
```python
g = (x for x in [1,3,5] if [5,7,9].count(x) > 0)
```

### 三、Python字符串和正则

字符串无所不在，字符串的处理也是最常见的操作。本章节将总结和字符串处理相关的一切操作。主要包括基本的字符串操作；高级字符串操作之正则。目前共有`20`个小例子

#### 1 反转字符串

```python
st="python"
#方法1
''.join(reversed(st))
#方法2
st[::-1]
```

#### 2 字符串切片操作

```python
字符串切片操作——查找替换3或5的倍数
In [1]:[str("java"[i%3*4:]+"python"[i%5*6:] or i) for i in range(1,15)]
OUT[1]:['1',
 '2',
 'java',
 '4',
 'python',
 'java',
 '7',
 '8',
 'java',
 'python',
 '11',
 'java',
 '13',
 '14']
```
#### 3 join串联字符串
```python
In [4]: mystr = ['1',
   ...:  '2',
   ...:  'java',
   ...:  '4',
   ...:  'python',
   ...:  'java',
   ...:  '7',
   ...:  '8',
   ...:  'java',
   ...:  'python',
   ...:  '11',
   ...:  'java',
   ...:  '13',
   ...:  '14']

In [5]: ','.join(mystr) #用逗号连接字符串
Out[5]: '1,2,java,4,python,java,7,8,java,python,11,java,13,14'
```

#### 4 字符串的字节长度

```python
def str_byte_len(mystr):
    return (len(mystr.encode('utf-8')))


str_byte_len('i love python')  # 13(个字节)
str_byte_len('字符')  # 6(个字节)
```



以下是正则部分

```python
import re
```

#### 1 查找第一个匹配串

```python
s = 'i love python very much'
pat = 'python' 
r = re.search(pat,s)
print(r.span()) #(7,13)
```

#### 2 查找所有1的索引

```python
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat,s)
for i in r:
    print(i)

# <re.Match object; span=(9, 10), match='1'>
# <re.Match object; span=(14, 15), match='1'>
```

#### 3 \d 匹配数字[0-9]
findall找出全部位置的所有匹配
```python
s = '一共20行代码运行时间13.59s'
pat = r'\d+' # +表示匹配数字(\d表示数字的通用字符)1次或多次
r = re.findall(pat,s)
print(r)
# ['20', '13', '59']
```

#### 4 匹配浮点数和整数

?表示前一个字符匹配0或1次
```python
s = '一共20行代码运行时间13.59s'
pat = r'\d+\.?\d+' # ?表示匹配小数点(\.)0次或1次，这种写法有个小bug，不能匹配到个位数的整数
r = re.findall(pat,s)
print(r)
# ['20', '13.59']

# 更好的写法：
pat = r'\d+\.\d+|\d+' # A|B，匹配A失败才匹配B
```
#### 5 ^匹配字符串的开头

```python
s = 'This module provides regular expression matching operations similar to those found in Perl'
pat = r'^[emrt]' # 查找以字符e,m,r或t开始的字符串
r = re.findall(pat,s)
print(r)
# [],因为字符串的开头是字符`T`，不在emrt匹配范围内，所以返回为空
IN [11]: s2 = 'email for me is guozhennianhua@163.com'
re.findall('^[emrt].*',s2)# 匹配以e,m,r,t开始的字符串，后面是多个任意字符
Out[11]: ['email for me is guozhennianhua@163.com']

```
#### 6 re.I 忽略大小写

```python
s = 'That'
pat = r't' 
r = re.findall(pat,s,re.I)
In [22]: r
Out[22]: ['T', 't']
```
#### 7 理解compile的作用
如果要做很多次匹配，可以先编译匹配串：
```python
import re
pat = re.compile('\W+') # \W 匹配不是数字和字母的字符
has_special_chars = pat.search('ed#2@edc') 
if has_special_chars:
    print(f'str contains special characters:{has_special_chars.group(0)}')

###输出结果: 
 # str contains special characters:#   

### 再次使用pat正则编译对象 做匹配
again_pattern = pat.findall('guozhennianhua@163.com')
if '@' in again_pattern:
    print('possibly it is an email')

```

#### 8 使用()捕获单词，不想带空格
使用`()`捕获
```python
s = 'This module provides regular expression matching operations similar to those found in Perl'
pat = r'\s([a-zA-Z]+)'  
r = re.findall(pat,s)
print(r) #['module', 'provides', 'regular', 'expression', 'matching', 'operations', 'similar', 'to', 'those', 'found', 'in', 'Perl']
```
看到提取单词中未包括第一个单词，使用`?`表示前面字符出现0次或1次，但是此字符还有表示贪心或非贪心匹配含义，使用时要谨慎。
```python
s = 'This module provides regular expression matching operations similar to those found in Perl'
pat = r'\s?([a-zA-Z]+)'  
r = re.findall(pat,s)
print(r) #['This', 'module', 'provides', 'regular', 'expression', 'matching', 'operations', 'similar', 'to', 'those', 'found', 'in', 'Perl']
```

#### 9 split分割单词
使用以上方法分割单词不是简洁的，仅仅是为了演示。分割单词最简单还是使用`split`函数。
```python
s = 'This module provides regular expression matching operations similar to those found in Perl'
pat = r'\s+'  
r = re.split(pat,s)
print(r) # ['This', 'module', 'provides', 'regular', 'expression', 'matching', 'operations', 'similar', 'to', 'those', 'found', 'in', 'Perl']

### 上面这句话也可直接使用str自带的split函数：
s.split(' ') #使用空格分隔

### 但是，对于风格符更加复杂的情况，split无能为力，只能使用正则

s = 'This,,,   module ; \t   provides|| regular ; '
words = re.split('[,\s;|]+',s)  #这样分隔出来，最后会有一个空字符串
words = [i for i in words if len(i)>0]
```

#### 10 match从字符串开始位置匹配
注意`match`,`search`等的不同：
1) match函数
```python
import re
### match
mystr = 'This'
pat = re.compile('hi')
pat.match(mystr) # None
pat.match(mystr,1) # 从位置1处开始匹配
Out[90]: <re.Match object; span=(1, 3), match='hi'>
```
2) search函数
search是从字符串的任意位置开始匹配
```python
In [91]: mystr = 'This'
    ...: pat = re.compile('hi')
    ...: pat.search(mystr)
Out[91]: <re.Match object; span=(1, 3), match='hi'>
```

#### 11 替换匹配的子串
`sub`函数实现对匹配子串的替换
```python
content="hello 12345, hello 456321"    
pat=re.compile(r'\d+') #要替换的部分
m=pat.sub("666",content)
print(m) # hello 666, hello 666
```

#### 12 贪心捕获
(.*)表示捕获任意多个字符，尽可能多的匹配字符
```python
content='<h>ddedadsad</h><div>graph</div>bb<div>math</div>cc'
pat=re.compile(r"<div>(.*)</div>")  #贪婪模式
m=pat.findall(content)
print(m) #匹配结果为： ['graph</div>bb<div>math']
```
#### 13 非贪心捕获
仅添加一个问号(`?`)，得到结果完全不同，这是非贪心匹配，通过这个例子体会贪心和非贪心的匹配的不同。
```python
content='<h>ddedadsad</h><div>graph</div>bb<div>math</div>cc'
pat=re.compile(r"<div>(.*?)</div>")
m=pat.findall(content)
print(m) # ['graph', 'math']
```
非贪心捕获，见好就收。

#### 14 常用元字符总结

    . 匹配任意字符  
    ^ 匹配字符串开始位置 
    $ 匹配字符串中结束的位置 
    * 前面的原子重复0次、1次、多次 
    ? 前面的原子重复0次或者1次 
    + 前面的原子重复1次或多次
    {n} 前面的原子出现了 n 次
    {n,} 前面的原子至少出现 n 次
    {n,m} 前面的原子出现次数介于 n-m 之间
    ( ) 分组,需要输出的部分

#### 15 常用通用字符总结

    \s  匹配空白字符 
    \w  匹配任意字母/数字/下划线 
    \W  和小写 w 相反，匹配任意字母/数字/下划线以外的字符
    \d  匹配十进制数字
    \D  匹配除了十进制数以外的值 
    [0-9]  匹配一个0-9之间的数字
    [a-z]  匹配小写英文字母
    [A-Z]  匹配大写英文字母

#### 14 密码安全检查

密码安全要求：1)要求密码为6到20位; 2)密码只包含英文字母和数字

```python
pat = re.compile(r'\w{6,20}') # 这是错误的，因为\w通配符匹配的是字母，数字和下划线，题目要求不能含有下划线
# 使用最稳的方法：\da-zA-Z满足`密码只包含英文字母和数字`
pat = re.compile(r'[\da-zA-Z]{6,20}')
```
选用最保险的`fullmatch`方法，查看是否整个字符串都匹配：
```python
pat.fullmatch('qaz12') # 返回 None, 长度小于6
pat.fullmatch('qaz12wsxedcrfvtgb67890942234343434') # None 长度大于22
pat.fullmatch('qaz_231') # None 含有下划线
pat.fullmatch('n0passw0Rd')
Out[4]: <re.Match object; span=(0, 10), match='n0passw0Rd'>
```

#### 15 爬取百度首页标题

```python
import re
from urllib import request

#爬虫爬取百度首页内容
data=request.urlopen("http://www.baidu.com/").read().decode()

#分析网页,确定正则表达式
pat=r'<title>(.*?)</title>'

result=re.search(pat,data)
print(result) <re.Match object; span=(1358, 1382), match='<title>百度一下，你就知道</title>'>

result.group() # 百度一下，你就知道
```

#### 16 批量转化为驼峰格式(Camel)

数据库字段名批量转化为驼峰格式

分析过程

```python
# 用到的正则串讲解
# \s 指匹配： [ \t\n\r\f\v]
# A|B：表示匹配A串或B串
# re.sub(pattern, newchar, string): 
# substitue代替，用newchar字符替代与pattern匹配的字符所有.
```



```python
# title(): 转化为大写，例子：
# 'Hello world'.title() # 'Hello World'
```



```python
# print(re.sub(r"\s|_|", "", "He llo_worl\td"))
s = re.sub(r"(\s|_|-)+", " ",
           'some_database_field_name').title().replace(" ", "")  
#结果： SomeDatabaseFieldName
```



```python
# 可以看到此时的第一个字符为大写，需要转化为小写
s = s[0].lower()+s[1:]  # 最终结果
```

 

整理以上分析得到如下代码：

```python
import re
def camel(s):
    s = re.sub(r"(\s|_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower() + s[1:]

# 批量转化
def batch_camel(slist):
    return [camel(s) for s in slist]
```

测试结果：

```python
s = batch_camel(['student_id', 'student\tname', 'student-add'])
print(s)
# 结果
['studentId', 'studentName', 'studentAdd']
```



### 四、Python文件

#### 1 获取后缀名

```python
import os
file_ext = os.path.splitext('./data/py/test.py')
front,ext = file_ext
In [5]: front
Out[5]: './data/py/test'

In [6]: ext
Out[6]: '.py'
```

#### 2 文件读操作

```python
import os
# 创建文件夹

def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
# 读取文件信息

def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist  # 返回读取内容
```



#### 3 文件写操作

```python
# 写入文件信息
# example1
# w写入，如果文件存在，则清空内容后写入，不存在则创建
f = open(r"./data/test.txt", "w", encoding="utf-8")
print(f.write("测试文件写入"))
f.close

# example2
# a写入，文件存在，则在文件内容后追加写入，不存在则创建
f = open(r"./data/test.txt", "a", encoding="utf-8")
print(f.write("测试文件写入"))
f.close

# example3
# with关键字系统会自动关闭文件和处理异常
with open(r"./data/test.txt", "w") as f:
    f.write("hello world!")
```



#### 4 路径中的文件名

```python
In [11]: import os
    ...: file_ext = os.path.split('./data/py/test.py')
    ...: ipath,ifile = file_ext
    ...:

In [12]: ipath
Out[12]: './data/py'

In [13]: ifile
Out[13]: 'test.py'
```



#### 5 批量修改文件后缀

**批量修改文件后缀**

本例子使用Python的`os`模块和 `argparse`模块，将工作目录`work_dir`下所有后缀名为`old_ext`的文件修改为后缀名为`new_ext`

通过本例子，大家将会大概清楚`argparse`模块的主要用法。

导入模块

```python
import argparse
import os
```

定义脚本参数

```python
def get_parser():
    parser = argparse.ArgumentParser(
        description='工作目录中文件后缀名修改')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='修改后缀名的文件目录')
    parser.add_argument('old_ext', metavar='OLD_EXT',
                        type=str, nargs=1, help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT',
                        type=str, nargs=1, help='新的后缀')
    return parser
```

后缀名批量修改

```python
def batch_rename(work_dir, old_ext, new_ext):
    """
    传递当前目录，原来后缀名，新的后缀名后，批量重命名后缀
    """
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为old_ext 的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重命名")
    print(os.listdir(work_dir))
```

实现Main

```python
def main():
    """
    main函数
    """
    # 命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())
    # 从命令行参数中依次解析出参数
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)
```



#### 6 xls批量转换成xlsx

```python
import os


def xls_to_xlsx(work_dir):
    """
    传递当前目录，原来后缀名，新的后缀名后，批量重命名后缀
    """
    old_ext, new_ext = '.xls', '.xlsx'
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为old_ext 的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重命名")
    print(os.listdir(work_dir))


xls_to_xlsx('./data')

# 输出结果：
# ['cut_words.csv', 'email_list.xlsx', 'email_test.docx', 'email_test.jpg', 'email_test.xlsx', 'geo_data.png', 'geo_data.xlsx',
'iotest.txt', 'pyside2.md', 'PySimpleGUI-4.7.1-py3-none-any.whl', 'test.txt', 'test_excel.xlsx', 'ziptest', 'ziptest.zip']
```



#### 7 定制文件不同行


比较两个文件在哪些行内容不同，返回这些行的编号，行号编号从1开始。

定义统计文件行数的函数

```python
# 统计文件个数
    def statLineCnt(statfile):
        print('文件名：'+statfile)
        cnt = 0
        with open(statfile, encoding='utf-8') as f:
            while f.readline():
                cnt += 1
            return cnt
```



统计文件不同之处的子函数：

```python
# more表示含有更多行数的文件
        def diff(more, cnt, less):
            difflist = []
            with open(less, encoding='utf-8') as l:
                with open(more, encoding='utf-8') as m:
                    lines = l.readlines()
                    for i, line in enumerate(lines):
                        if line.strip() != m.readline().strip():
                            difflist.append(i)
            if cnt - i > 1:
                difflist.extend(range(i + 1, cnt))
            return [no+1 for no in difflist]
```



主函数：

```python
# 返回的结果行号从1开始
# list表示fileA和fileB不同的行的编号

def file_diff_line_nos(fileA, fileB):
    try:
        cntA = statLineCnt(fileA)
        cntB = statLineCnt(fileB)
        if cntA > cntB:
            return diff(fileA, cntA, fileB)
        return diff(fileB, cntB, fileA)

    except Exception as e:
        print(e)
```

比较两个文件A和B，拿相对较短的文件去比较，过滤行后的换行符`\n`和空格。

暂未考虑某个文件最后可能有的多行空行等特殊情况

使用`file_diff_line_nos` 函数：

```python
if __name__ == '__main__':
    import os
    print(os.getcwd())

    '''
    例子：
    fileA = "'hello world!!!!''\
            'nice to meet you'\
            'yes'\
            'no1'\
            'jack'"
    fileB = "'hello world!!!!''\
            'nice to meet you'\
            'yes' "
    '''
    diff = file_diff_line_nos('./testdir/a.txt', './testdir/b.txt')
    print(diff)  # [4, 5]
```

关于文件比较的，实际上，在Python中有对应模块`difflib` , 提供更多其他格式的文件更详细的比较，大家可参考：

> https://docs.python.org/3/library/difflib.html?highlight=difflib#module-difflib



#### 8 获取指定后缀名的文件

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

r = find_file('.','md') 
print(r) # 返回所有目录下的md文件
```


#### 9 批量获取文件修改时间

```python
# 获取目录下文件的修改时间
import os
from datetime import datetime

print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def get_modify_time(indir):
    for root, _, files in os.walk(indir):  # 循环D:\works目录和子目录
        for file in files:
            absfile = os.path.join(root, file)
            modtime = datetime.fromtimestamp(os.path.getmtime(absfile))
            now = datetime.now()
            difftime = now-modtime
            if difftime.days < 20:  # 条件筛选超过指定时间的文件
                print(f"""{absfile}
                    修改时间[{modtime.strftime('%Y-%m-%d %H:%M:%S')}]
                    距今[{difftime.days:3d}天{difftime.seconds//3600:2d}时{difftime.seconds%3600//60:2d}]"""
                      )  # 打印相关信息


get_modify_time('./data')
```

    打印效果：
    当前时间：2019-12-22 16:38:53
    ./data\cut_words.csv
                        修改时间[2019-12-21 10:34:15]
                        距今[  1天 6时 4]
    当前时间：2019-12-22 16:38:53
    ./data\cut_words.csv
                        修改时间[2019-12-21 10:34:15]
                        距今[  1天 6时 4]
    ./data\email_test.docx
                        修改时间[2019-12-03 07:46:29]
                        距今[ 19天 8时52]
    ./data\email_test.jpg
                        修改时间[2019-12-03 07:46:29]
                        距今[ 19天 8时52]
    ./data\email_test.xlsx
                        修改时间[2019-12-03 07:46:29]
                        距今[ 19天 8时52]
    ./data\iotest.txt
                        修改时间[2019-12-13 08:23:18]
                        距今[  9天 8时15]
    ./data\pyside2.md
                        修改时间[2019-12-05 08:17:22]
                        距今[ 17天 8时21]
    ./data\PySimpleGUI-4.7.1-py3-none-any.whl
                        修改时间[2019-12-05 00:25:47]
                        距今[ 17天16时13]

#### 10 批量压缩文件


```python
import zipfile  # 导入zipfile,这个是用来做压缩和解压的Python模块；
import os
import time


def batch_zip(start_dir):
    start_dir = start_dir  # 要压缩的文件夹路径
    file_news = start_dir + '.zip'  # 压缩后文件夹的名字

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = dir_path.replace(start_dir, '')
        f_path = f_path and f_path + os.sep  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news


batch_zip('./data/ziptest')


```

#### 11 32位加密

```python
import hashlib
# 对字符串s实现32位加密


def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()


print(hash_cry32(1))  # c4ca4238a0b923820dcc509a6f75849b
print(hash_cry32('hello'))  # 5d41402abc4b2a76b9719d911017c592
```



### 五、Python日期

Python日期章节，由表示大日期的`calendar`, `date`模块，逐渐过渡到表示时间刻度更小的模块：`datetime`, `time`模块，按照此逻辑展开，总结了最常用的`9`个关于时间处理模块的例子。



#### 1 年的日历图

```python
import calendar
from datetime import date
mydate = date.today()
year_calendar_str = calendar.calendar(2019)
print(f"{mydate.year}年的日历图：{year_calendar_str}\n")
```

打印结果：

```python
2019

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                   1  2  3
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       4  5  6  7  8  9 10
14 15 16 17 18 19 20      11 12 13 14 15 16 17      11 12 13 14 15 16 17
21 22 23 24 25 26 27      18 19 20 21 22 23 24      18 19 20 21 22 23 24
28 29 30 31               25 26 27 28               25 26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7             1  2  3  4  5                      1  2
 8  9 10 11 12 13 14       6  7  8  9 10 11 12       3  4  5  6  7  8  9
15 16 17 18 19 20 21      13 14 15 16 17 18 19      10 11 12 13 14 15 16
22 23 24 25 26 27 28      20 21 22 23 24 25 26      17 18 19 20 21 22 23
29 30                     27 28 29 30 31            24 25 26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                         1
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       2  3  4  5  6  7  8
15 16 17 18 19 20 21      12 13 14 15 16 17 18       9 10 11 12 13 14 15
22 23 24 25 26 27 28      19 20 21 22 23 24 25      16 17 18 19 20 21 22
29 30 31                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31
```



#### 2 判断是否为闰年

```python
import calendar
from datetime import date

mydate = date.today()
is_leap = calendar.isleap(mydate.year)
print_leap_str = "%s年是闰年" if is_leap else "%s年不是闰年\n"
print(print_leap_str % mydate.year)
```

打印结果：

```python
2019年不是闰年
```

#### 3 月的日历图

```python
import calendar
from datetime import date

mydate = date.today()
month_calendar_str = calendar.month(mydate.year, mydate.month)

print(f"{mydate.year}年-{mydate.month}月的日历图：{month_calendar_str}\n")
```

打印结果：

```python
December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

#### 4 月有几天

```python
import calendar
from datetime import date

mydate = date.today()
weekday, days = calendar.monthrange(mydate.year, mydate.month)
print(f'{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday}天\n')
print(f'{mydate.year}年-{mydate.month}月共有{days}天\n')
```

打印结果：

```python
2019年-12月的第一天是那一周的第6天

2019年-12月共有31天
```



#### 5 月第一天

```python
from datetime import date
mydate = date.today()
month_first_day = date(mydate.year, mydate.month, 1)
print(f"当月第一天:{month_first_day}\n")
```

打印结果：

```python
当月第一天:2019-12-01
```



#### 6 月最后一天

```python
from datetime import date
import calendar
mydate = date.today()
_, days = calendar.monthrange(mydate.year, mydate.month)
month_last_day = date(mydate.year, mydate.month, days)
print(f"当月最后一天:{month_last_day}\n")
```

打印结果：

```python
当月最后一天:2019-12-31
```



#### 7 获取当前时间

```python
from datetime import date, datetime
from time import localtime

today_date = date.today()
print(today_date)  # 2019-12-22

today_time = datetime.today()
print(today_time)  # 2019-12-22 18:02:33.398894

local_time = localtime()
print(strftime("%Y-%m-%d %H:%M:%S", local_time))  # 转化为定制的格式 2019-12-22 18:13:41
```



#### 8 字符时间转时间

```python
from time import strptime

# parse str time to struct time
struct_time = strptime('2019-12-22 10:10:08', "%Y-%m-%d %H:%M:%S")
print(struct_time) # struct_time类型就是time中的一个类

# time.struct_time(tm_year=2019, tm_mon=12, tm_mday=22, tm_hour=10, tm_min=10, tm_sec=8, tm_wday=6, tm_yday=356, tm_isdst=-1)
```



#### 9 时间转字符时间

```python
from time import strftime, strptime, localtime

In [2]: print(localtime()) #这是输入的时间
Out[2]: time.struct_time(tm_year=2019, tm_mon=12, tm_mday=22, tm_hour=18, tm_min=24, tm_sec=56, tm_wday=6, tm_yday=356, tm_isdst=0)

print(strftime("%m-%d-%Y %H:%M:%S", localtime()))  # 转化为定制的格式
# 这是字符串表示的时间：   12-22-2019 18:26:21
```



### 六、Python利器
Python中的三大利器包括：`迭代器`，`生成器`，`装饰器`，利用好它们才能开发出最高性能的Python程序，涉及到的内置模块 `itertools`提供迭代器相关的操作。此部分收录有意思的例子共计`14`例。


#### 1 寻找第n次出现位置

```python
def search_n(s, c, n):
    size = 0
    for i, x in enumerate(s):
        if x == c:
            size += 1
        if size == n:
            return i
    return -1



print(search_n("fdasadfadf", "a", 3))# 结果为7，正确
print(search_n("fdasadfadf", "a", 30))# 结果为-1，正确
```


#### 2 斐波那契数列前n项

```python
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


list(fibonacci(5))  # [1, 1, 2, 3, 5]
```

#### 3 找出所有重复元素

```python
from collections import Counter


def find_all_duplicates(lst):
    c = Counter(lst)
    return list(filter(lambda k: c[k] > 1, c))


find_all_duplicates([1, 2, 2, 3, 3, 3])  # [2,3]
```

#### 4 联合统计次数
Counter对象间可以做数学运算

```python
from collections import Counter
a = ['apple', 'orange', 'computer', 'orange']
b = ['computer', 'orange']

ca = Counter(a)
cb = Counter(b)
#Counter对象间可以做数学运算
ca + cb  # Counter({'orange': 3, 'computer': 2, 'apple': 1})


# 进一步抽象，实现多个列表内元素的个数统计


def sumc(*c):
    if (len(c) < 1):
        return
    mapc = map(Counter, c)
    s = Counter([])
    for ic in mapc: # ic 是一个Counter对象
        s += ic
    return s


#Counter({'orange': 3, 'computer': 3, 'apple': 1, 'abc': 1, 'face': 1})
sumc(a, b, ['abc'], ['face', 'computer'])

```

#### 5 groupby单字段分组

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

#### 6 itemgetter和key函数

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

#### 7 groupby多字段分组

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

#### 8 sum函数计算和聚合同时做

Python中的聚合类函数`sum`,`min`,`max`第一个参数是`iterable`类型，一般使用方法如下：

```python
a = [4,2,5,1]
sum([i+1 for i in a]) # 16
```

使用列表生成式`[i+1 for i in a]`创建一个长度与`a`一行的临时列表，这步完成后，再做`sum`聚合。

试想如果你的数组`a`长度十百万级，再创建一个这样的临时列表就很不划算，最好是一边算一边聚合，稍改动为如下：

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

#### 9 list分组(生成器版)

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

#### 10 列表全展开（生成器版）
```python
#多层列表展开成单层列表
a=[1,2,[3,4,[5,6],7],8,["python",6],9]
def function(lst):
    for i in lst:
        if type(i)==list:
            yield from function(i)
        else:
            yield i
print(list(function(a))) # [1, 2, 3, 4, 5, 6, 7, 8, 'python', 6, 9]
```

#### 11 测试函数运行时间的装饰器
```python
#测试函数执行时间的装饰器示例
import time
def timing_func(fn):
    def wrapper():
        start=time.time()
        fn()   #执行传入的fn参数
        stop=time.time()
        return (stop-start)
    return wrapper
@timing_func
def test_list_append():
    lst=[]
    for i in range(0,100000):
        lst.append(i)  
@timing_func
def test_list_compre():
    [i for i in range(0,100000)]  #列表生成式
a=test_list_append()
c=test_list_compre()
print("test list append time:",a)
print("test list comprehension time:",c)
print("append/compre:",round(a/c,3))

test list append time: 0.0219423770904541
test list comprehension time: 0.007980823516845703
append/compre: 2.749
```

#### 12 统计异常出现次数和时间的装饰器


写一个装饰器，统计某个异常重复出现指定次数时，经历的时长。
```python
import time
import math


def excepter(f):
    i = 0
    t1 = time.time()
    def wrapper(): 
        try:
            f()
        except Exception as e:
            nonlocal i
            i += 1
            print(f'{e.args[0]}: {i}')
            t2 = time.time()
            if i == n:
                print(f'spending time:{round(t2-t1,2)}')
    return wrapper

```

关键词`nonlocal`常用于函数嵌套中，声明变量i为非局部变量；

如果不声明，`i+=1`表明`i`为函数`wrapper`内的局部变量，因为在`i+=1`引用(reference)时,`i`未被声明，所以会报`unreferenced variable`的错误。

使用创建的装饰函数`excepter`, `n`是异常出现的次数。

共测试了两类常见的异常：`被零除`和`数组越界`。

```python
n = 10 # except count

@excepter
def divide_zero_except():
    time.sleep(0.1)
    j = 1/(40-20*2)

# test zero divived except
for _ in range(n):
    divide_zero_except()


@excepter
def outof_range_except():
    a = [1,3,5]
    time.sleep(0.1)
    print(a[3])
# test out of range except
for _ in range(n):
    outof_range_except()

```

打印出来的结果如下：
```python
division by zero: 1
division by zero: 2
division by zero: 3
division by zero: 4
division by zero: 5
division by zero: 6
division by zero: 7
division by zero: 8
division by zero: 9
division by zero: 10
spending time:1.01
list index out of range: 1
list index out of range: 2
list index out of range: 3
list index out of range: 4
list index out of range: 5
list index out of range: 6
list index out of range: 7
list index out of range: 8
list index out of range: 9
list index out of range: 10
spending time:1.01
```


#### 13 测试运行时长的装饰器


```python
#测试函数执行时间的装饰器示例
import time
def timing(fn):
    def wrapper():
        start=time.time()
        fn()   #执行传入的fn参数
        stop=time.time()
        return (stop-start)
    return wrapper

@timing
def test_list_append():
    lst=[]
    for i in range(0,100000):
        lst.append(i)  

@timing
def test_list_compre():
    [i for i in range(0,100000)]  #列表生成式

a=test_list_append()
c=test_list_compre()
print("test list append time:",a)
print("test list comprehension time:",c)
print("append/compre:",round(a/c,3))

# test list append time: 0.0219
# test list comprehension time: 0.00798
# append/compre: 2.749
```



#### 14 装饰器通俗理解

再看一个装饰器：

```python
def call_print(f):
  def g():
    print('you\'re calling %s function'%(f.__name__,))
  return g
```

使用`call_print`装饰器：

```python
@call_print
def myfun():
  pass
 
@call_print
def myfun2():
  pass
```

myfun()后返回：

```python
In [27]: myfun()
you're calling myfun function

In [28]: myfun2()
you're calling myfun2 function
```

**使用call_print**

你看，`@call_print`放置在任何一个新定义的函数上面，都会默认输出一行，你正在调用这个函数的名。

这是为什么呢？注意观察新定义的`call_print`函数(加上@后便是装饰器):

```python
def call_print(f):
  def g():
    print('you\'re calling %s function'%(f.__name__,))
  return g
```

它必须接受一个函数`f`，然后返回另外一个函数`g`.

**装饰器本质**

本质上，它与下面的调用方式效果是等效的：

```
def myfun():
  pass

def myfun2():
  pass
  
def call_print(f):
  def g():
    print('you\'re calling %s function'%(f.__name__,))
  return g
```

下面是最重要的代码：

```
myfun = call_print(myfun)
myfun2 = call_print(myfun2)
```

大家看明白吗？也就是call_print(myfun)后不是返回一个函数吗，然后再赋值给myfun.

再次调用myfun, myfun2时，效果是这样的：

```python
In [32]: myfun()
you're calling myfun function

In [33]: myfun2()
you're calling myfun2 function
```

你看，这与装饰器的实现效果是一模一样的。装饰器的写法可能更加直观些，所以不用显示的这样赋值：`myfun = call_print(myfun)`，`myfun2 = call_print(myfun2)`，但是装饰器的这种封装，猛一看，有些不好理解。

#### 15 定制递减迭代器

```python
#编写一个迭代器，通过循环语句，实现对某个正整数的依次递减1，直到0.
class Descend(Iterator):
    def __init__(self,N):
        self.N=N
        self.a=0
    def __iter__(self):
        return self 
    def __next__(self):
        while self.a<self.N:
            self.N-=1
            return self.N
        raise StopIteration
    
descend_iter=Descend(10)
print(list(descend_iter))
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

核心要点：

1 `__nex__ `名字不能变，实现定制的迭代逻辑

2 `raise StopIteration`：通过 raise 中断程序，必须这样写



### 七、Python画图

Python常用的绘图工具包括：`matplotlib`, `seaborn`, `plotly`等，以及一些其他专用于绘制某类图如词云图等的包，描绘绘图轨迹的`turtle`包等。本章节将会使用一些例子由易到难的阐述绘图的经典小例子，目前共收录`10`个。

#### 1 turtle绘制奥运五环图

turtle绘图的函数非常好用，基本看到函数名字，就能知道它的含义，下面使用turtle，仅用15行代码来绘制奥运五环图。

1 导入库

```python
import turtle as p
```

2 定义画圆函数

```python
def drawCircle(x,y,c='red'):
    p.pu()# 抬起画笔
    p.goto(x,y) # 绘制圆的起始位置
    p.pd()# 放下画笔
    p.color(c)# 绘制c色圆环
    p.circle(30,360) #绘制圆：半径，角度
```

3 画笔基本设置

```python
p = turtle
p.pensize(3) # 画笔尺寸设置3
```

4 绘制五环图

调用画圆函数

```python
drawCircle(0,0,'blue')
drawCircle(60,0,'black')
drawCircle(120,0,'red')
drawCircle(90,-30,'green')
drawCircle(30,-30,'yellow')    

p.done()
```

结果：

![](./img/turtle1.png)

#### 2 turtle绘制漫天雪花


导入模块

导入 `turtle`库和 python的 `random`

```python
import turtle as p
import random
```

绘制雪花

```python
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

```

绘制地面

```python
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
```

主函数

```python
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


动态图结果展示：


<img src="./img/turtlesnow.gif" alt="Sample"  width="600" height="300">

#### 3 wordcloud词云图


```python
import hashlib
import pandas as pd
from wordcloud import WordCloud
geo_data=pd.read_excel(r"../data/geo_data.xlsx")
print(geo_data)
# 0     深圳
# 1     深圳
# 2     深圳
# 3     深圳
# 4     深圳
# 5     深圳
# 6     深圳
# 7     广州
# 8     广州
# 9     广州

words = ','.join(x for x in geo_data['city'] if x != []) #筛选出非空列表值
wc = WordCloud(
    background_color="green", #背景颜色"green"绿色
    max_words=100, #显示最大词数
    font_path='./fonts/simhei.ttf', #显示中文
    min_font_size=5,
    max_font_size=100,
    width=500  #图幅宽度
    )
x = wc.generate(words)
x.to_file('../data/geo_data.png')
```

![](./data/geo_data.png)



#### 4 plotly画柱状图和折线图



```python
#柱状图+折线图
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5],
        y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
    ))
fig.add_trace(
    go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[2, 0.5, 0.7, -1.2, 0.3, 0.4]
    ))
fig.show()
```

<img src="./img/plotly1.png" alt="Sample"  width="600" height="300">


#### 5 seaborn热力图

```python
# 导入库
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 生成数据集
data = np.random.random((6,6))
np.fill_diagonal(data,np.ones(6))
features = ["prop1","prop2","prop3","prop4","prop5", "prop6"]
data = pd.DataFrame(data, index = features, columns=features)
print(data)
# 绘制热力图
heatmap_plot = sns.heatmap(data, center=0, cmap='gist_rainbow')
plt.show()
```


<img src="./img/heatmap.png" alt="Sample"  width="600" height="300">

#### 6 matplotlib折线图

模块名称：example_utils.py，里面包括三个函数，各自功能如下：

```python
import matplotlib.pyplot as plt

# 创建画图fig和axes
def setup_axes():
    fig, axes = plt.subplots(ncols=3, figsize=(6.5,3))
    for ax in fig.axes:
        ax.set(xticks=[], yticks=[])
    fig.subplots_adjust(wspace=0, left=0, right=0.93)
    return fig, axes
# 图片标题
def title(fig, text, y=0.9):
    fig.suptitle(text, size=14, y=y, weight='semibold', x=0.98, ha='right',
                 bbox=dict(boxstyle='round', fc='floralwhite', ec='#8B7E66',
                           lw=2))
# 为数据添加文本注释
def label(ax, text, y=0):
    ax.annotate(text, xy=(0.5, 0.00), xycoords='axes fraction', ha='center',
                style='italic',
                bbox=dict(boxstyle='round', facecolor='floralwhite',
                          ec='#8B7E66'))
```

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25BicBcb6EQVsWlJcZwBJyQzH3RRjsHl5TELibR1AiaVc8VdTpe4SuKiagibdqqjNV8R5iclic44AZnTjPzg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

```python
import numpy as np
import matplotlib.pyplot as plt

import example_utils

x = np.linspace(0, 10, 100)

fig, axes = example_utils.setup_axes()
for ax in axes:
    ax.margins(y=0.10)

# 子图1 默认plot多条线，颜色系统分配
for i in range(1, 6):
    axes[0].plot(x, i * x)

# 子图2 展示线的不同linestyle
for i, ls in enumerate(['-', '--', ':', '-.']):
    axes[1].plot(x, np.cos(x) + i, linestyle=ls)

# 子图3 展示线的不同linestyle和marker
for i, (ls, mk) in enumerate(zip(['', '-', ':'], ['o', '^', 's'])):
    axes[2].plot(x, np.cos(x) + i * x, linestyle=ls, marker=mk, markevery=10)

# 设置标题
# example_utils.title(fig, '"ax.plot(x, y, ...)": Lines and/or markers', y=0.95)
# 保存图片
fig.savefig('plot_example.png', facecolor='none')
# 展示图片
plt.show()
```



#### 7 matplotlib散点图
![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25BicBcb6EQVsWlJcZwBJyQzS3KTX8YzWzkPvDIiaIibsxHDz2C93qwpoFRqiaL6EVeSFibAT04ggxNbHA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

对应代码：

```python
"""
散点图的基本用法
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils

# 随机生成数据
np.random.seed(1874)
x, y, z = np.random.normal(0, 1, (3, 100))
t = np.arctan2(y, x)
size = 50 * np.cos(2 * t)**2 + 10

fig, axes = example_utils.setup_axes()

# 子图1
axes[0].scatter(x, y, marker='o',  color='darkblue', facecolor='white', s=80)
example_utils.label(axes[0], 'scatter(x, y)')

# 子图2
axes[1].scatter(x, y, marker='s', color='darkblue', s=size)
example_utils.label(axes[1], 'scatter(x, y, s)')

# 子图3
axes[2].scatter(x, y, s=size, c=z,  cmap='gist_ncar')
example_utils.label(axes[2], 'scatter(x, y, s, c)')

# example_utils.title(fig, '"ax.scatter(...)": Colored/scaled markers',
#                     y=0.95)
fig.savefig('scatter_example.png', facecolor='none')

plt.show()
```



#### 8 matplotlib柱状图

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25BicBcb6EQVsWlJcZwBJyQzzBv3R8fHsVV6mEcV1KALF5u927OjdAwyhS4NUVHAAhlsBeC24zCricg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

对应代码：

```python
import numpy as np
import matplotlib.pyplot as plt

import example_utils


def main():
    fig, axes = example_utils.setup_axes()

    basic_bar(axes[0])
    tornado(axes[1])
    general(axes[2])

    # example_utils.title(fig, '"ax.bar(...)": Plot rectangles')
    fig.savefig('bar_example.png', facecolor='none')
    plt.show()

# 子图1
def basic_bar(ax):
    y = [1, 3, 4, 5.5, 3, 2]
    err = [0.2, 1, 2.5, 1, 1, 0.5]
    x = np.arange(len(y))
    ax.bar(x, y, yerr=err, color='lightblue', ecolor='black')
    ax.margins(0.05)
    ax.set_ylim(bottom=0)
    example_utils.label(ax, 'bar(x, y, yerr=e)')

# 子图2
def tornado(ax):
    y = np.arange(8)
    x1 = y + np.random.random(8) + 1
    x2 = y + 3 * np.random.random(8) + 1
    ax.barh(y, x1, color='lightblue')
    ax.barh(y, -x2, color='salmon')
    ax.margins(0.15)
    example_utils.label(ax, 'barh(x, y)')

# 子图3
def general(ax):
    num = 10
    left = np.random.randint(0, 10, num)
    bottom = np.random.randint(0, 10, num)
    width = np.random.random(num) + 0.5
    height = np.random.random(num) + 0.5
    ax.bar(left, height, width, bottom, color='salmon')
    ax.margins(0.15)
    example_utils.label(ax, 'bar(l, h, w, b)')


main()
```

#### 9 matplotlib等高线图


<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25BicBcb6EQVsWlJcZwBJyQzMGnSAHhCHG1bNEWHh1VJcmYN8E1ZBjPaL5iclH2HrvyYmCuDeibbfV3A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

对应代码：

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data

import example_utils

z = np.load(get_sample_data('bivariate_normal.npy'))

fig, axes = example_utils.setup_axes()

axes[0].contour(z, cmap='gist_earth')
example_utils.label(axes[0], 'contour')

axes[1].contourf(z, cmap='gist_earth')
example_utils.label(axes[1], 'contourf')

axes[2].contourf(z, cmap='gist_earth')
cont = axes[2].contour(z, colors='black')
axes[2].clabel(cont, fontsize=6)
example_utils.label(axes[2], 'contourf + contour\n + clabel')

# example_utils.title(fig, '"contour, contourf, clabel": Contour/label 2D data',
#                     y=0.96)
fig.savefig('contour_example.png', facecolor='none')

plt.show()
```

#### 10 imshow图

![](https://camo.githubusercontent.com/7d73ce5053864430bc8b2d7191870889c848106b/68747470733a2f2f6d6d62697a2e717069632e636e2f6d6d62697a5f706e672f46516438675163794e32354269634263623645515673576c4a635a77424a79517a6b4647626963707879753858727774784d73314e466177656d35696369627a6f4c716f356d7364353847343965477a6e3455304247554261772f3634303f77785f666d743d706e672674703d7765627026777866726f6d3d352677785f6c617a793d312677785f636f3d31)

对应代码：

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data
from mpl_toolkits import axes_grid1

import example_utils


def main():
    fig, axes = setup_axes()
    plot(axes, *load_data())
    # example_utils.title(fig, '"ax.imshow(data, ...)": Colormapped or RGB arrays')
    fig.savefig('imshow_example.png', facecolor='none')
    plt.show()


def plot(axes, img_data, scalar_data, ny):

    # 默认线性插值
    axes[0].imshow(scalar_data, cmap='gist_earth', extent=[0, ny, ny, 0])

    # 最近邻插值
    axes[1].imshow(scalar_data, cmap='gist_earth', interpolation='nearest',
                   extent=[0, ny, ny, 0])

    # 展示RGB/RGBA数据
    axes[2].imshow(img_data)


def load_data():
    img_data = plt.imread(get_sample_data('5.png'))
    ny, nx, nbands = img_data.shape
    scalar_data = np.load(get_sample_data('bivariate_normal.npy'))
    return img_data, scalar_data, ny


def setup_axes():
    fig = plt.figure(figsize=(6, 3))
    axes = axes_grid1.ImageGrid(fig, [0, 0, .93, 1], (1, 3), axes_pad=0)

    for ax in axes:
        ax.set(xticks=[], yticks=[])
    return fig, axes


main()
```

#### 11 pyecharts绘制仪表盘

使用pip install pyecharts 安装，版本为 v1.6，pyecharts绘制仪表盘，只需要几行代码：

```python
from pyecharts import charts

# 仪表盘
gauge = charts.Gauge()
gauge.add('Python小例子', [('Python机器学习', 30), ('Python基础', 70.),
                        ('Python正则', 90)])
gauge.render(path="./data/仪表盘.html")
print('ok')
```

仪表盘中共展示三项，每项的比例为30%,70%,90%，如下图默认名称显示第一项：Python机器学习，完成比例为30%

<img src="./img/image-20191228194635902.png" alt="Sample"  width="600" height="450">

#### 12 pyecharts漏斗图

```python
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page
from random import randint

def funnel_base() -> Funnel:
  c = (
    Funnel()
    .add("豪车", [list(z) for z in zip(['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉'],
                 [randint(1, 20) for _ in range(7)])])
    .set_global_opts(title_opts=opts.TitleOpts(title="豪车漏斗图"))
  )
  return c
funnel_base().render('./img/car_fnnel.html')
```

以7种车型及某个属性值绘制的漏斗图，属性值大越靠近漏斗的大端。

<img src="https://i.loli.net/2019/12/28/aCGfBp6YIvWqU84.png" alt="Sample"  width="600" height="300">

#### 13 pyecharts日历图

```python
import datetime
import random
from pyecharts import options as opts
from pyecharts.charts import Calendar

def calendar_interval_1() -> Calendar:
    begin = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 12, 27)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range(0, (end - begin).days + 1, 2)  # 隔天统计
    ]
    calendar = (
      Calendar(init_opts=opts.InitOpts(width="1200px")).add(
            "", data, calendar_opts=opts.CalendarOpts(range_="2019"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2019年步数统计"),
            visualmap_opts=opts.VisualMapOpts(
                max_=25000,
                min_=1000,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return calendar

calendar_interval_1().render('./img/calendar.html')
```

绘制2019年1月1日到12月27日的步行数，官方给出的图形宽度`900px`不够，只能显示到9月份，本例使用`opts.InitOpts(width="1200px")`做出微调，并且`visualmap`显示所有步数，每隔一天显示一次：

![](https://i.loli.net/2019/12/28/Zw9mWM1QtUVjCgn.png)

#### 14 pyecharts绘制graph图

```python
import json
import os
from pyecharts import options as opts
from pyecharts.charts import Graph, Page

def graph_base() -> Graph:
    nodes = [
        {"name": "cus1", "symbolSize": 10},
        {"name": "cus2", "symbolSize": 30},
        {"name": "cus3", "symbolSize": 20}
    ]
    links = []
    for i in nodes:
        if i.get('name') == 'cus1':
            continue
        for j in nodes:
            if j.get('name') == 'cus1':
                continue
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="customer-influence"))
    )
    return c
```

构建图，其中客户点1与其他两个客户都没有关系(`link`)，也就是不存在有效边：

![](https://i.loli.net/2019/12/28/ts4WrTQINSaHdM1.png)

#### 15 pyecharts水球图

```python
from pyecharts import options as opts
from pyecharts.charts import Liquid, Page
from pyecharts.globals import SymbolType

def liquid() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.67, 0.30, 0.15])
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid"))
    )
    return c

liquid().render('./img/liquid.html')
```

水球图的取值`[0.67, 0.30, 0.15]`表示下图中的`三个波浪线`，一般代表三个百分比:

<img src="./img/liquid.gif" alt="Sample"  width="600" height="450">

#### 16 pyecharts饼图

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
from random import randint

def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉'],
                                       [randint(1, 20) for _ in range(7)])])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

pie_base().render('./img/pie_pyecharts.html')
```
<img src="./img/20191229105841.png" alt="Sample"  width="600" height="350">


#### 17 pyecharts极坐标图

```python
import random
from pyecharts import options as opts
from pyecharts.charts import Page, Polar

def polar_scatter0() -> Polar:
    data = [(alpha, random.randint(1, 100)) for alpha in range(101)] # r = random.randint(1, 100)
    print(data)
    c = (
        Polar()
        .add("", data, type_="bar", label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar"))
    )
    return c

polar_scatter0().render('./img/polar.html')
```

极坐标表示为`(夹角,半径)`，如(6,94)表示夹角为6，半径94的点：

<img src="https://i.loli.net/2019/12/28/QxVOFuDB5y6wgpJ.png" alt="Sample"  width="600" height="500">

#### 18 pyecharts词云图

```python
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType

words = [
    ("Python", 100),
    ("C++", 80),
    ("Java", 95),
    ("R", 50),
    ("JavaScript", 79),
    ("C", 65)
]

def wordcloud() -> WordCloud:
    c = (
        WordCloud()
        # word_size_range: 单词字体大小范围
        .add("", words, word_size_range=[20, 100], shape='cardioid')
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud"))
    )
    return c

wordcloud().render('./img/wordcloud.html')
```

`("C",65)`表示在本次统计中C语言出现65次


<img src="https://i.loli.net/2019/12/28/nSs8MY9Dc4I1egk.png" alt="Sample"  width="600" height="300">

#### 19 pyecharts系列柱状图

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from random import randint

def bar_series() -> Bar:
    c = (
        Bar()
        .add_xaxis(['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉'])
        .add_yaxis("销量", [randint(1, 20) for _ in range(7)])
        .add_yaxis("产量", [randint(1, 20) for _ in range(7)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar的主标题", subtitle="Bar的副标题"))
    )
    return c

bar_series().render('./img/bar_series.html')
```

<img src="https://i.loli.net/2019/12/28/egamLZw2oMHA19T.png" alt="Sample"  width="600" height="300">

#### 20 pyecharts热力图

```python
import random
from pyecharts import options as opts
from pyecharts.charts import HeatMap

def heatmap_car() -> HeatMap:
    x = ['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉']
    y = ['中国','日本','南非','澳大利亚','阿根廷','阿尔及利亚','法国','意大利','加拿大']
    value = [[i, j, random.randint(0, 100)]
             for i in range(len(x)) for j in range(len(y))]
    c = (
        HeatMap()
        .add_xaxis(x)
        .add_yaxis("销量", y, value)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c

heatmap_car().render('./img/heatmap_pyecharts.html')
```

热力图描述的实际是三维关系，x轴表示车型，y轴表示国家，每个色块的颜色值代表销量，颜色刻度尺显示在左下角，颜色越红表示销量越大。


<img src="./img/image-20191229101724665.png" alt="Sample"  width="600" height="300">



#### 21 matplotlib绘制动画

`matplotlib`是python中最经典的绘图包，里面`animation`模块能绘制动画。

首先导入小例子使用的模块：
```python
from matplotlib import pyplot as plt
from matplotlib import animation
from random import randint, random
```

生成数据，`frames_count`是帧的个数，`data_count`每个帧的柱子个数

```python
class Data:
    data_count = 32
    frames_count = 2

    def __init__(self, value):
        self.value = value
        self.color = (0.5, random(), random()) #rgb

    # 造数据
    @classmethod
    def create(cls):
        return [[Data(randint(1, cls.data_count)) for _ in range(cls.data_count)]
                for frame_i in range(cls.frames_count)]
```

绘制动画：`animation.FuncAnimation`函数的回调函数的参数`fi`表示第几帧，注意要调用`axs.cla()`清除上一帧。

```python
def draw_chart():
    fig = plt.figure(1, figsize=(16, 9))
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])

    # 生成数据
    frames = Data.create()

    def animate(fi):
        axs.cla()  # clear last frame
        axs.set_xticks([])
        axs.set_yticks([])
        return axs.bar(list(range(Data.data_count)),        # X
                       [d.value for d in frames[fi]],       # Y
                       1,                                   # width
                       color=[d.color for d in frames[fi]]  # color
                       )
    # 动画展示
    anim = animation.FuncAnimation(fig, animate, frames=len(frames))
    plt.show()


draw_chart()
```

### 八：Python实用工具

#### 1 一行代码优化输出的异常信息

```python
pip install pretty-errors
```

写一个函数测试：

```python
def divided_zero():
    for i in range(10, -1, -1):
        print(10/i)


divided_zero()
```

在没有import这个`pretty-errors`前，输出的错误信息有些冗余：

```python
Traceback (most recent call last):
  File "c:\Users\HUAWEI\.vscode\extensions\ms-python.python-2019.11.50794\pythonFiles\ptvsd_launcher.py", line 43, in <module>
    main(ptvsdArgs)
  File "c:\Users\HUAWEI\.vscode\extensions\ms-python.python-2019.11.50794\pythonFiles\lib\python\old_ptvsd\ptvsd\__main__.py",
line 432, in main
    run()
  File "c:\Users\HUAWEI\.vscode\extensions\ms-python.python-2019.11.50794\pythonFiles\lib\python\old_ptvsd\ptvsd\__main__.py",
line 316, in run_file
    runpy.run_path(target, run_name='__main__')
  File "D:\anaconda3\lib\runpy.py", line 263, in run_path
    pkg_name=pkg_name, script_name=fname)
  File "D:\anaconda3\lib\runpy.py", line 96, in _run_module_code
    mod_name, mod_spec, pkg_name, script_name)
  File "D:\anaconda3\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "d:\source\sorting-visualizer-master\sorting\debug_test.py", line 6, in <module>
    divided_zero()
  File "d:\source\sorting-visualizer-master\sorting\debug_test.py", line 3, in divided_zero
    print(10/i)
ZeroDivisionError: division by zero
```

我们使用刚安装的`pretty_errors`，`import`下:

```python
import pretty_errors

def divided_zero():
    for i in range(10, -1, -1):
        print(10/i)

divided_zero()
```

此时看看输出的错误信息，非常精简只有2行，去那些冗余信息：

```python
ZeroDivisionError:
division by zero
```

完整的输出信息如下图片所示：



![image-20200104103849047](./img/image-20200104103849047.png)

#### 2 两行代码实现旋转和缩放图像

首先安装pillow:

```python
pip install pillow
```

旋转图像下面图像45度：

![](./img/plotly2.png)

```python
In [1]: from PIL import Image
In [2]: im = Image.open('./img/plotly2.png')
In [4]: im.rotate(45).show()
```

旋转45度后的效果图

![image-20200105085120611](./img/image-20200105085120611.png)

等比例缩放图像：

```python
im.thumbnail((128,72),Image.ANTIALIAS)
```

缩放后的效果图：

![](./img/pillow_suofang.png)



过滤图像后的效果图：

```python
from PIL import ImageFilter
im.filter(ImageFilter.CONTOUR).show()
```

![](./img/pillow_filter.png)

### 九、Python实战


#### 1 环境搭建

区分几个小白容易混淆的概念：pycharm，python解释器，conda安装，pip安装，总结来说：

- `pycharm`是python开发的集成开发环境(Integrated Development Environment，简称IDE)，它本身无法执行Python代码
- `python解释器`才是真正执行代码的工具，pycharm里可设置Python解释器，一般去python官网下载python3.7或python3.8版本；如果安装过`anaconda`，它里面必然也包括一个某版本的Python解释器；pycharm配置python解释器选择哪一个都可以。
- anaconda是python常用包的合集，并提供给我们使用`conda`命令非常方便的安装各种Python包。
- `conda安装`：我们安装过anaconda软件后，就能够使用conda命令下载anaconda源里(比如中科大镜像源)的包
- `pip安装`：类似于conda安装的python安装包的方法

**修改镜像源**

在使用安装`conda` 安装某些包会出现慢或安装失败问题，最有效方法是修改镜像源为国内镜像源。之前都选用清华镜像源，但是2019年后已停止服务。推荐选用中科大镜像源。

先查看已经安装过的镜像源，cmd窗口执行命令：

```python
conda config --show
```

查看配置项`channels`，如果显示带有`tsinghua`，则说明已安装过清华镜像。

```python
channels:
- https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/cpu/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
```

下一步，使用`conda config --remove channels url地址 `删除清华镜像，如下命令删除第一个。然后，依次删除所有镜像源

```python
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/cpu/
```

添加目前可用的中科大镜像源：

```
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
```

并设置搜索时显示通道地址：

```python
conda config --set show_channel_urls yes
```

确认是否安装镜像源成功，执行`conda config --show`，找到`channels`值为如下：

```
channels:
  - https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
  - defaults
```

Done~

#### 2 自动群发邮件

Python自动群发邮件

```python
import smtplib
from email import (header)
from email.mime import (text, application, multipart)
import time

def sender_mail():
    smt_p = smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com', port=25)
    sender, password = '113097485@qq.com', "**************"
    smt_p.login(sender, password)
    receiver_addresses, count_num = [
        'guozhennianhua@163.com', 'xiaoxiazi99@163.com'], 1
    for email_address in receiver_addresses:
        try:
            msg = multipart.MIMEMultipart()
            msg['From'] = "zhenguo"
            msg['To'] = email_address
            msg['subject'] = header.Header('这是邮件主题通知', 'utf-8')
            msg.attach(text.MIMEText(
                '这是一封测试邮件，请勿回复本邮件~', 'plain', 'utf-8'))
            smt_p.sendmail(sender, email_address, msg.as_string())
            time.sleep(10)
            print('第%d次发送给%s' % (count_num, email_address))
            count_num = count_num + 1
        except Exception as e:
            print('第%d次给%s发送邮件异常' % (count_num, email_address))
            continue
    smt_p.quit()

sender_mail()
```



注意：
发送邮箱是qq邮箱，所以要在qq邮箱中设置开启SMTP服务，设置完成时会生成一个授权码，将这个授权码赋值给文中的`password`变量。



发送后的截图：



![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25N30MmbE2PjM2F1j86EUFfdzva26tvlwVpR2MGEcLXJvjWQ8v3BrzEwmFxpjia4zohfzbkDBpnNjg/640?wx_fmt=png)



#### 3 二分搜索

二分搜索是程序员必备的算法，无论什么场合，都要非常熟练地写出来。

小例子描述：
在**有序数组**`arr`中，指定区间`[left,right]`范围内，查找元素`x`
如果不存在，返回`-1`

二分搜索`binarySearch`实现的主逻辑

```python
def binarySearch(arr, left, right, x):
    while left <= right:

        mid = int(left + (right - left) / 2); # 找到中间位置。求中点写成(left+right)/2更容易溢出，所以不建议这样写

        # 检查x是否出现在位置mid
        if arr[mid] == x:
            print('found %d 在索引位置%d 处' %(x,mid))
            return mid

            # 假如x更大，则不可能出现在左半部分
        elif arr[mid] < x:
            left = mid + 1 #搜索区间变为[mid+1,right]
            print('区间缩小为[%d,%d]' %(mid+1,right))

        # 同理，假如x更小，则不可能出现在右半部分
        elif x<arr[mid]:
            right = mid - 1 #搜索区间变为[left,mid-1]
            print('区间缩小为[%d,%d]' %(left,mid-1))

    # 假如搜索到这里，表明x未出现在[left,right]中
    return -1
```

在`Ipython`交互界面中，调用`binarySearch`的小Demo:

```python
In [8]: binarySearch([4,5,6,7,10,20,100],0,6,5)
区间缩小为[0,2]
found 5 at 1
Out[8]: 1

In [9]: binarySearch([4,5,6,7,10,20,100],0,6,4)
区间缩小为[0,2]
区间缩小为[0,0]
found 4 at 0
Out[9]: 0

In [10]: binarySearch([4,5,6,7,10,20,100],0,6,20)
区间缩小为[4,6]
found 20 at 5
Out[10]: 5

In [11]: binarySearch([4,5,6,7,10,20,100],0,6,100)
区间缩小为[4,6]
区间缩小为[6,6]
found 100 at 6
Out[11]: 6
```

#### 4 爬取天气数据并解析温度值

爬取天气数据并解析温度值

素材来自朋友袁绍，感谢！

爬取的html 结构

![](./img/1.png)

```python
import requests
from lxml import etree
import pandas as pd
import re

url = 'http://www.weather.com.cn/weather1d/101010100.shtml#input'
with requests.get(url) as res:
    content = res.content
    html = etree.HTML(content)
```



通过lxml模块提取值

lxml比beautifulsoup解析在某些场合更高效

```python
location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
temperature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')
```

结果：

```python
['香河', '涿州', '唐山', '沧州', '天津', '廊坊', '太原', '石家庄', '涿鹿', '张家口', '保定', '三河', '北京孔庙', '北京国子监', '中国地质博物馆', '月坛公
园', '明城墙遗址公园', '北京市规划展览馆', '什刹海', '南锣鼓巷', '天坛公园', '北海公园', '景山公园', '北京海洋馆']

['11/-5°C', '14/-5°C', '12/-6°C', '12/-5°C', '11/-1°C', '11/-5°C', '8/-7°C', '13/-2°C', '8/-6°C', '5/-9°C', '14/-6°C', '11/-4°C', '13/-3°C'
, '13/-3°C', '12/-3°C', '12/-3°C', '13/-3°C', '12/-2°C', '12/-3°C', '13/-3°C', '12/-2°C', '12/-2°C', '12/-2°C', '12/-3°C']
```


构造DataFrame对象

```python
df = pd.DataFrame({'location':location, 'temperature':temperature})
print('温度列')
print(df['temperature'])
```

正则解析温度值

```python
df['high'] = df['temperature'].apply(lambda x: int(re.match('(-?[0-9]*?)/-?[0-9]*?°C', x).group(1) ) )
df['low'] = df['temperature'].apply(lambda x: int(re.match('-?[0-9]*?/(-?[0-9]*?)°C', x).group(1) ) )
print(df)
```

详细说明子字符创捕获

除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用`()`表示的就是要提取的分组（group）。比如：`^(\d{3})-(\d{3,8})$`分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码

```python
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 010-12345
# 010
# 12345
```

如果正则表达式中定义了组，就可以在`Match`对象上用`group()`方法提取出子串来。

注意到`group(0)`永远是原始字符串，`group(1)`、`group(2)`……表示第1、2、……个子串。


最终结果

```python
Name: temperature, dtype: object
    location temperature  high  low
0         香河     11/-5°C    11   -5
1         涿州     14/-5°C    14   -5
2         唐山     12/-6°C    12   -6
3         沧州     12/-5°C    12   -5
4         天津     11/-1°C    11   -1
5         廊坊     11/-5°C    11   -5
6         太原      8/-7°C     8   -7
7        石家庄     13/-2°C    13   -2
8         涿鹿      8/-6°C     8   -6
9        张家口      5/-9°C     5   -9
10        保定     14/-6°C    14   -6
11        三河     11/-4°C    11   -4
12      北京孔庙     13/-3°C    13   -3
13     北京国子监     13/-3°C    13   -3
14   中国地质博物馆     12/-3°C    12   -3
15      月坛公园     12/-3°C    12   -3
16   明城墙遗址公园     13/-3°C    13   -3
17  北京市规划展览馆     12/-2°C    12   -2
18       什刹海     12/-3°C    12   -3
19      南锣鼓巷     13/-3°C    13   -3
20      天坛公园     12/-2°C    12   -2
21      北海公园     12/-2°C    12   -2
22      景山公园     12/-2°C    12   -2
23     北京海洋馆     12/-3°C    12   -3
```



#### 5  制作小而美的计算器

1)  ui设计

使用`qt designer` ，按装anaconda后，在如下路径找到：

> conda3.05\Library\bin

`designer.exe`文件，双击启动：

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25fl867daHB4tcw6K1Tcoicia73PibMMgfnm3I5DrS5IeqAehYZDpAqJ4Euia40Wnaf9Kr4qDrBWgMemw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

创建窗体，命名为`XiaoDing`，整个的界面如下所示：

![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25fl867daHB4tcw6K1TcoiciaVdvX5Y9Zxh82jzm2YvT23wXTuaMTqKX4RzSic3zVULMPIUO5Fy5LMDw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

`qt 设计器`提供的常用控件基本都能满足开发需求，通过拖动左侧的控件，很便捷的就能搭建出如下的UI界面，比传统的手写控件代码要方便很多。

最终设计的计算器`XiaoDing`界面如下，

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25fl867daHB4tcw6K1TcoicianCCIiaNlXy5ugv1blJ83KDUrvuTq9icB3hN6zXUy5rib1ITLibgeUxiaOCQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

比如，其中一个用于计算器显示的对象：`lcdNumber`，对象的类型为：`LCD Number`。右侧为计算器中用到的所有对象。

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25fl867daHB4tcw6K1Tcoicia9syg40IVicTZ6PqYGVa21aRIhicuCFygibVSXRTdLApn00ticG6pIPibADQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25fl867daHB4tcw6K1TcoiciabNVLAb7Nicu2sb4YREYU5HbvII8K8CdVibXC5TNrN29Th6jWqEDRxLqA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  >

2)  转py文件

使用如下命令，将设计好的`ui`文件转为`py`文件：

```python
pyuic5 -o ./calculator/MainWindow.py ./calculator/mainwindow.ui
```

3)  计算器实现逻辑

导入库：

```python
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from MainWindow import Ui_MainWindow
```

主题代码逻辑很精简：

```python
# Calculator state.
READY = 0
INPUT = 1


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Setup numbers.
        for n in range(0, 10):
            getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))

        # Setup operations.
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv))  # operator.div for Python2.7

        self.pushButton_pc.pressed.connect(self.operation_pc)
        self.pushButton_eq.pressed.connect(self.equals)

        # Setup actions
        self.actionReset.triggered.connect(self.reset)
        self.pushButton_ac.pressed.connect(self.reset)

        self.actionExit.triggered.connect(self.close)

        self.pushButton_m.pressed.connect(self.memory_store)
        self.pushButton_mr.pressed.connect(self.memory_recall)

        self.memory = 0
        self.reset()

        self.show()
```



基础方法：

```python
    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v

        self.display()

    def display(self):
        self.lcdNumber.display(self.stack[-1])
```

按钮`RE`,`M`, `RE`对应的实现逻辑：

```python
    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    def memory_store(self):
        self.memory = self.lcdNumber.value()

    def memory_recall(self):
        self.state = INPUT
        self.stack[-1] = self.memory
        self.display()
```



`+`,`-`,`x`,`/`,`/100`对应实现方法：

```python
def operation(self, op):
        if self.current_op:  # Complete the current operation
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def operation_pc(self):
        self.state = INPUT
        self.stack[-1] *= 0.01
        self.display()
```

`=`号对应的方法实现：

```python
 def equals(self):
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            try:
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                self.lcdNumber.display('Err')
                self.stack = [0]
            else:
                self.current_op = None
                self.state = READY
                self.display()
```

main函数：

```python
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("XiaoDing")

    window = MainWindow()
    app.exec_()
```

<img src="https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN25fl867daHB4tcw6K1TcoiciaxZtJBDMfcgJAvnCWHCad74mLjrkX97EFolhUjdOucTK6tqgw2PaziaQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1" alt="Sample"  width="600" height="300">

### 十、 Python基础算法

#### 1 领略算法魅力

深刻研究排序算法是入门算法较为好的一种方法，现在还记得4年前手动实现常见8种排序算法，通过随机生成一些数据，逐个校验代码实现的排序过程是否与预期的一致，越做越有劲，越有劲越想去研究，公交车上，吃饭的路上。。。那些画面，现在依然记忆犹新。

能力有限，当时并没有生成排序过程的动画，所以这些年想着抽时间一定把排序的过程都制作成动画，然后分享出来，让更多的小伙伴看到，通过排序算法的动态演示动画，找到学习算法的真正乐趣，从而迈向一个新的认知领域。

当时我还是用C++写的，时过境迁，Python迅速崛起，得益于Python的简洁，接口易用，最近终于有人在github中开源了使用Python动画展示排序算法的项目，真是倍感幸运。

动画还是用matplotlib做出来的，这就更完美了，一边学完美的算法，一边还能提升Python熟练度，一边还能学到使用matplotlib制作动画。

快速排序动画展示

![img](https://mmbiz.qpic.cn/mmbiz_gif/FQd8gQcyN256Z0UkwIAVsP1pMsIUYTaHibX8xewf1Sgyvfh3VAR7IkWdwQtbNsniaiaXHzjG0Tcefl3Dv4OibhbGeg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

归并排序动画展示


![img](https://mmbiz.qpic.cn/mmbiz_gif/FQd8gQcyN256Z0UkwIAVsP1pMsIUYTaHpD5ibgM0kmia30zVM163X3RF9HnX2icibkJNghcibfjicxbibIJLLYprxqOqw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

堆排序动画展示

![img](https://mmbiz.qpic.cn/mmbiz_gif/FQd8gQcyN256Z0UkwIAVsP1pMsIUYTaH7HenTzoiaicwFrMTCiav18yLEhPmXombelTAlAMeBhzic4icnsuoQg1D7sw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

这些算法动画使用Matplotlib制作，接下来逐个补充。

#### 2 排序算法的动画展示

学会第一部分如何制作动画后，可将此技术应用于排序算法调整过程的动态展示上。

首先生成测试使用的数据，待排序的数据个数至多`20个`，待排序序列为`random_wait_sort`，为每个值赋一个颜色值，这个由`random_rgb`负责：

```python
data_count = 20  # here, max value of data_count is 20

random_wait_sort = [12, 34, 32, 24, 28, 39, 5,
                    22, 11, 25, 33, 32, 1, 25, 3, 8, 7, 1, 34, 7]

random_rgb = [(0.5, 0.811565104942967, 0.11211028937187217),
              (0.5, 0.5201323831224014, 0.6660999602342474),
              (0.5, 0.575976663060455, 0.17788242607567772),
              (0.5, 0.6880174797416493, 0.43581701833249353),
              (0.5, 0.4443131322001743, 0.6993600264279745),
              (0.5, 0.5538835821863523, 0.889276053938713),
              (0.5, 0.4851681185146841, 0.7977608586163772),
              (0.5, 0.3886717808488436, 0.09319137949618972),
              (0.5, 0.8952456581687489, 0.8282376936934484),
              (0.5, 0.16360202854998007, 0.4538892160157194),
              (0.5, 0.23233400128809478, 0.8544141586189615),
              (0.5, 0.5224648797546528, 0.8194014475829123),
              (0.5, 0.49396099968405016, 0.47441724394796825),
              (0.5, 0.12078104526714728, 0.7715022079860492),
              (0.5, 0.19428498518228154, 0.08174917157481443),
              (0.5, 0.6058698403873457, 0.6085936584142663),
              (0.5, 0.7801178568951216, 0.6414767240649862),
              (0.5, 0.4768865661174162, 0.3889866229610085),
              (0.5, 0.4301945092238082, 0.961688141676841),
              (0.5, 0.40496648895289855, 0.24234095882836093)]


```

再封装一个简单的数据对象`Data`：
```python
class Data:
    def __init__(self, value, rgb):
        self.value = value
        self.color = rgb

    # 造数据
    @classmethod
    def create(cls):
        return [Data(val, rgb) for val, rgb in zip(random_wait_sort[:data_count],
                                                   random_rgb[:data_count])]
```


#### 3 先拿冒泡实验

一旦发生调整，我们立即保存到帧列表`frames`中，注意此处需要`deepcopy`:
```python
# 冒泡排序
def bubble_sort(waiting_sort_data):
    frames = [waiting_sort_data]
    ds = copy.deepcopy(waiting_sort_data)
    for i in range(data_count-1):
        for j in range(data_count-i-1):
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] = ds[j+1], ds[j]
                frames.append(copy.deepcopy(ds))
    frames.append(ds)
    return frames
```

实验结果图：

![image-20200104232411426](./img/image-20200104232411426.png)

完整动画演示：

![img](./img/bubble_sort.gif)

#### 4 快速排序
先上代码，比较经典，值得回味：
```python
def quick_sort(data_set):
    frames = [data_set]
    ds = copy.deepcopy(data_set)

    def qsort(head, tail):
        if tail - head > 1:
            i = head
            j = tail - 1
            pivot = ds[j].value
            while i < j:
                if ds[i].value > pivot or ds[j].value < pivot:
                    ds[i], ds[j] = ds[j], ds[i]
                    frames.append(copy.deepcopy(ds))
                if ds[i].value == pivot:
                    j -= 1
                else:
                    i += 1
            qsort(head, i)
            qsort(i+1, tail)

    qsort(0, data_count)
    frames.append(ds)
    return frames
```
快速排序算法对输入为随机的序列优势往往较为明显，同样的输入数据，它只需要`24`帧调整就能完成排序：

![image-20200104232337713](./img/image-20200104232337713.png)

#### 5 选择排序
选择排序和堆排序都是选择思维，但是性能却不如堆排序：
```python
def selection_sort(data_set):
    frames = [data_set]
    ds = copy.deepcopy(data_set)
    for i in range(0, data_count-1):
        for j in range(i+1, data_count):
            if ds[j].value < ds[i].value:
                ds[i], ds[j] = ds[j], ds[i]
                frames.append(copy.deepcopy(ds))

    frames.append(ds)
    return frames
```
同样的输入数据，它完成排序需要`108`帧:

![image-20200104232448531](./img/image-20200104232448531.png)



动画展示如下，每轮会从未排序的列表中，挑出一个最小值，放到已排序序列后面。

![img](./img/select_sort.gif)

#### 6 堆排序
堆排序大大改进了选择排序，逻辑上使用二叉树，先建立一个大根堆，然后根节点与未排序序列的最后一个元素交换，重新对未排序序列建堆。

完整代码如下：

```python
def heap_sort(data_set):
    frames = [data_set]
    ds = copy.deepcopy(data_set)

    def heap_adjust(head, tail):
        i = head * 2 + 1  # head的左孩子
        while i < tail:
            if i + 1 < tail and ds[i].value < ds[i+1].value:  # 选择一个更大的孩子
                i += 1
            if ds[i].value <= ds[head].value:
                break
            ds[head], ds[i] = ds[i], ds[head]
            frames.append(copy.deepcopy(ds))
            head = i
            i = i * 2 + 1

    # 建立一个最大堆，从最后一个父节点开始调整
    for i in range(data_count//2-1, -1, -1):
        heap_adjust(i, data_count)
    for i in range(data_count-1, 0, -1):
        ds[i], ds[0] = ds[0], ds[i]  # 把最大值放在位置i处
        heap_adjust(0, i)  # 从0~i-1进行堆调整
    frames.append(ds)
    return frames
```
堆排序的性能也比较优秀，完成排序需要51次调整。

![image-20200104232824967](./img/image-20200104232824967.png)


#### 7 综合
依次调用以上常见的4种排序算法，分别保存所有帧和html文件。

```python
waiting_sort_data = Data.create()
for sort_method in [bubble_sort, quick_sort, selection_sort, heap_sort]:
    frames = sort_method(waiting_sort_data)
    draw_chart(frames, file_name='%s.html' % (sort_method.__name__,))
```

获取以上完整代码、所有数据文件、结果文件：[完整源码下载](./data/sort.zip)

---

### 十一、 Python机器学习

#### 1 引言

机器学习是一个目标函数优化问题，给定目标函数f，约束条件会有一般包括以下三类：

1. 仅含等式约束
2. 仅含不等式约束
3. 等式和不等式约束混合型

当然还有一类没有任何约束条件的最优化问题

关于最优化问题，大都令人比较头疼，首先大多教材讲解通篇都是公式，各种符号表达，各种梯度，叫人看的云里雾里。

有没有结合几何图形阐述以上问题的？很庆幸，还真有这么好的讲解材料，图文并茂，逻辑推导严谨，更容易叫我们理解`拉格朗日乘数法`、`KKT条件`为什么就能求出极值。



#### 2 仅含等式约束
假定目标函数是连续可导函数，问题定义如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceYcFHnQksH3ZgF0CMYp1s4cYPR5YialMQs46trGjicgxPALHC1rN4mXKg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuycelRpUBuNQwJj5oQQ8QktOBibCIbcxbVWTxnFye14m5iazoxEst88K9Dng/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)


通过以上方法求解此类问题，但是为什么它能求出极值呢？

#### 3 找找感觉

大家时间都有限，只列出最核心的逻辑，找找sense, 如有兴趣可回去下载PPT仔细体会。

此解释中对此类问题的定义：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/FQd8gQcyN27HY2RsrOicg569iaLUpVuycetLx0gaA8qGQNFfz8ZXYw1QaLoAXm1jwIWwNGlyicfBBkOntG9WMs0og/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

为了更好的阐述，给定一个具体例子，锁定：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceQibFRulITicamVH6pTOiaHdDV89INiaicuQMRX86OjpcDw9YmawZPVLEUPw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



所以，f(x)的一系列取值包括0,1,100,10000等任意实数：



![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceqWZr7hU6PhKqvJeXN00xKUCJlnGfqUYtO5pDHN2P5xyNtzshkgaicjg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



但是，约束条件`h(x)`注定会约束`f(x)`不会等于100，不会等于10000...



![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceTVCgwQsk315dxdQmS0W2iaPib2RqpfRdH0UlCZ9gIYu1pJ53uQV53JJw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



一个可行点：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceUBWaFUWkpxlz7gQpAY5TgBZ894g1BlrcOfPIBfgPflib19hLYr2cSDA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 4 梯度下降

我们想要寻找一个移动`x`的规则，使得移动后`f(x+delta_x)`变小，当然必须满足约束`h(x+delta_x)=0`

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyce3EhmMq1dMhA8rnpDVoia6a3JHhPFVkavEEQhafPsEQP6MEHHkcSgbSA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)使得`f(x`)减小最快的方向就是它的梯度反方向，即

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyce6UFsJgA0M8JbjMbed2FDkjT6JNuibcDSqz9N3VibVRz2JHiblEZZRAtfw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_jpg/FQd8gQcyN27HY2RsrOicg569iaLUpVuycesXN0ECXHs3hK234unbUuwywWnibSSbicl7I6EP2u3yOfRliaaRQUxz5dg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

因此，要想f(x+delta_x) 变小，通过图形可以看出，只要保持和梯度反方向夹角小于90，也就是保持大概一个方向，`f(x+delta_x)`就会变小，转化为公式就是：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceiafpfo06d42FaVfAGNQw808GmGt5ib4az1CwqxY2rHay5vkBAFj8FeEA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如下所示的一个`delta_x`就是一个会使得f(x)减小的方向，但是这种移动将会破坏等式约束: `h(x)=0`，关于准确的移动方向下面第四小节会讲到

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyce1C04y8Vs2TPJkV8icVibbFbsp2qW7w3bzaOZWXneIicxrnjUdLcVoQtCQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 5 约束面的法向



约束面的外法向：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceBPOeoyXLxpWk6OIZ0PygC7WNWjZpeyWx6qGia1jMLwrDefopyXJ0QAw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceNmQ9UjdT4hdhXCBEiaG4PEdAjFIvhJVxzBrjxvvrtk8MRLZtuIJwZgQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

约束面的内法向：



![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyce2krGLNt1rgAZAxHicnTIwGFnZbTgXlygrZ8Nsv5sBRnSXHpAlxOaaeg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

绿圈表示法向的`正交`方向

**x沿着绿圈内的方向移动，将会使得f(x)减小，同时满足等式约束h(x) = 0**

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyce9PeBl0GkZl4EhgmOia4mRBIwkHTSNys4EicEZ72AK0GTQ1kqer9N1AhQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 6 大胆猜想



 我们不妨大胆假设，如果满足下面的条件：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuycexjAPibEn1A66IOCicUL3icXrvb1dFxnjF8icKQrW8S9SxqmEj7xWMfoSYw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

根据第四小节讲述，`delta_x`必须正交于`h(x)`，所以：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceyArqYEDONMoVIDnIVegSx0kAw9KWLBs66826FMCMI0O5WaiciaOzFs9w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

所以：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceMgoOhRcZ5SOrD58hVGLoVWzps5sZnFAaJGiaCBw1kk4PtdXrLPTCxww/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

至此，我们就找到`f(x)`偏导数等于0的点，就是下图所示的**两个关键点（它们也是f(x)与h(x)的临界点）**。且必须满足以下条件，也就是两个向量必须是平行的：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuycexjAPibEn1A66IOCicUL3icXrvb1dFxnjF8icKQrW8S9SxqmEj7xWMfoSYw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)![img](https://mmbiz.qpic.cn/mmbiz_jpg/FQd8gQcyN27HY2RsrOicg569iaLUpVuyceTIibaXbFCX7scIH5QGvpjO2PyNpEvycqdJCa3bzL3qbCwS5NpchZrfw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### 7 完全解码拉格朗日乘数法

至此，已经完全解码拉格朗日乘数法，拉格朗日巧妙的构造出下面这个式子：

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuyce6Zsbhc8Iqu3xlHicQbqsaHHb4LI0mhNWujJc8yKwHhr2iaoBshRoBSCA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**还有取得极值的的三个条件，都是对以上五个小节中涉及到的条件的编码**

![img](https://mmbiz.qpic.cn/mmbiz_png/FQd8gQcyN27HY2RsrOicg569iaLUpVuycesnKeAia8p5OmzibRzujsVic15TXUXH8QzHQXP7gl0AcXDiaAn7ARoicsvkQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

关于第三个条件，稍加说明。

对于含有多个变量，比如本例子就含有2个变量`x1`, `x2`，就是一个多元优化问题，需要求二阶导，二阶导的矩阵就被称为`海塞矩阵`（Hessian Matrix）

与求解一元问题一样，仅凭一阶导数等于是无法判断极值的，需要求二阶导，并且二阶导大于0才是极小值，小于0是极大值，等于0依然无法判断是否在此点去的极值。



> 以上就是机器学习最常用的优化技巧：拉格朗日乘数法的图形讲解，相信大家已经找到一定感觉，接下来几天我们通过例子，详细阐述机器学习的具体概念，常用算法，使用Python实现主要的算法，使用Sklearn，Kaggle数据实战这些算法。



#### 8 均匀分布

导入本次实验所用的4种常见分布，连续分布的代表：`beta`分布、`正态`分布，`均匀`分布，离散分布的代表：`二项`分布。

绘图装饰器带有四个参数分别表示`legend`的2类说明文字，y轴label, 保存的png文件名称。

```python
import pretty_errors
import numpy as np
from scipy.stats import beta, norm, uniform, binom
import matplotlib.pyplot as plt
from functools import wraps

# 定义带四个参数的画图装饰器

def my_plot(label0=None, label1=None, ylabel='probability density function', fn=None):
    def decorate(f):
        @wraps(f)
        def myplot():
            fig = plt.figure(figsize=(16, 9))
            ax = fig.add_subplot(111)
            x, y, y1 = f()
            ax.plot(x, y, linewidth=2, c='r', label=label0)
            ax.plot(x, y1, linewidth=2, c='b', label=label1)
            ax.legend()
            plt.ylabel(ylabel)
            # plt.show()
            plt.savefig('./img/%s' % (fn,))
            print('%s保存成功' % (fn,))
            plt.close()
        return myplot
    return decorate
```

```python
# 均匀分布(uniform)
@my_plot(label0='b-a=1.0', label1='b-a=2.0', fn='uniform.png')
def unif():
    x = np.arange(-0.01, 2.01, 0.01)
    y = uniform.pdf(x, loc=0.0, scale=1.0)
    y1 = uniform.pdf(x, loc=0.0, scale=2.0)
    return x, y, y1
```

![](./img/uniform.png)

#### 9 **二项分布**

红色曲线表示发生一次概率为0.3，重复50次的密度函数，二项分布期望值为0.3*50 = 15次。看到这50次实验，很可能出现的次数为10~20.可与蓝色曲线对比分析。

```python
# 二项分布
@my_plot(label0='n=50,p=0.3', label1='n=50,p=0.7', fn='binom.png', ylabel='probability mass function')
def bino():
    x = np.arange(50)
    n, p, p1 = 50, 0.3, 0.7
    y = binom.pmf(x, n=n, p=p)
    y1 = binom.pmf(x, n=n, p=p1)
    return x, y, y1
```

![](./img/binom.png)

#### 10 高斯分布

红色曲线表示均值为0，标准差为1.0的概率密度函数，蓝色曲线的标准差更大，所以它更矮胖，显示出取值的多样性，和不稳定性。

```python
# 高斯 分布
@my_plot(label0='u=0.,sigma=1.0', label1='u=0.,sigma=2.0', fn='guass.png')
def guass():
    x = np.arange(-5, 5, 0.1)
    y = norm.pdf(x, loc=0.0, scale=1.0)
    y1 = norm.pdf(x, loc=0., scale=2.0)
    return x, y, y1
```

![](./img/guass.png)

#### 11 beta分布

beta分布的期望值如下，可从下面的两条曲线中加以验证：

![image-20200105205845965](./img/image-20200105205845965.png)

```python
# beta 分布
@my_plot(label0='a=10., b=30.', label1='a=4., b=4.', fn='beta.png')
def bet():
    x = np.arange(-0.01, 1, 0.001)
    y = beta.pdf(x, a=10., b=30.)
    y1 = beta.pdf(x, a=4., b=4.)
    return x, y, y1
```

![](./img/beta.png)