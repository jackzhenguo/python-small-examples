### 六、 Python 坑点和工具

#### 185 含单个元素的元组

Python中有些函数的参数类型为元组，其内有1个元素，这样创建是错误的：

```python
c = (5) # NO!
```

它实际创建一个整型元素5，必须要在元素后加一个`逗号`:

```python
c = (5,) # YES!
```

#### 186 默认参数设为空

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

#### 187 共享变量未绑定之坑

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

#### 188 lambda自由参数之坑

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

#### 189 各种参数使用之坑

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

#### 190 列表删除之坑

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

#### 191 列表快速复制之坑

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

#### 192 字符串驻留

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

#### 193 相同值的不可变对象

```python
In [5]: d = {}
    ...: d[1] = 'java'
    ...: d[1.0] = 'python'

In [6]: d
Out[6]: {1: 'python'}

### key=1,value=java的键值对神奇消失了
In [7]: d[1]
Out[7]: 'python'
In [8]: d[1.0]
Out[8]: 'python'
```

这是因为具有相同值的不可变对象在Python中始终具有`相同的哈希值`

由于存在`哈希冲突`，不同值的对象也可能具有相同的哈希值。

#### 194 对象销毁顺序

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

#### 195 充分认识for

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

#### 196 认识执行时机

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

#### 197 创建空集合错误

这是Python的一个集合：`{1,3,5}`，它里面没有重复元素，在去重等场景有重要应用。下面这样创建空集合是错误的：

```python
empty = {} #NO!
```

cpython会解释它为字典

使用内置函数`set()`创建空集合：

```python
empty = set() #YES!
```

#### 198 pyecharts传入Numpy数据绘图失败

echarts使用广泛，echarts+python结合后的包：pyecharts，同样可很好用，但是传入Numpy的数据，像下面这样绘图会失败：

```python
from pyecharts.charts import Bar
import pyecharts.options as opts
import numpy as np
c = (
    Bar()
    .add_xaxis([1, 2, 3, 4, 5])
    # 传入Numpy数据绘图失败！
    .add_yaxis("商家A", np.array([0.1, 0.2, 0.3, 0.4, 0.5]))
)

c.render()
```

<img src="../img/image-20200129164119080.png" width="50%"/>

由此可见pyecharts对Numpy数据绘图不支持，传入原生Python的list:

```python
from pyecharts.charts import Bar
import pyecharts.options as opts
import numpy as np
c = (
    Bar()
    .add_xaxis([1, 2, 3, 4, 5])
    # 传入Python原生list
    .add_yaxis("商家A", np.array([0.1, 0.2, 0.3, 0.4, 0.5]).tolist())
)

c.render()
```

<img src="../img/image-20200129164339971.png" width="50%"/>

#### 199 优化代码异常输出包

一行代码优化输出的异常信息

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



<img src="../img/image-20200104103849047.png" width="50%"/>

#### 200 图像处理包pillow

两行代码实现旋转和缩放图像

首先安装pillow:

```python
pip install pillow
```

旋转图像下面图像45度：

<img src="../img/plotly2.png" width="40%"/>

```python
In [1]: from PIL import Image
In [2]: im = Image.open('./img/plotly2.png')
In [4]: im.rotate(45).show()
```

旋转45度后的效果图

<img src="../img/image-20200105085120611.png" width="40%"/>

等比例缩放图像：

```python
im.thumbnail((128,72),Image.ANTIALIAS)
```

缩放后的效果图：

![](E:\guozhen3\资料库\06self\python-small-examples\chs\pillow_suofang.png)



过滤图像后的效果图：

```python
from PIL import ImageFilter
im.filter(ImageFilter.CONTOUR).show()
```

<img src="../img/pillow_filter.png" width="40%"/>

#### 201 一行代码找到编码

兴高采烈地，从网页上抓取一段 `content`

但是，一 `print ` 就不那么兴高采烈了，结果看到一串这个：

```markdown
b'\xc8\xcb\xc9\xfa\xbf\xe0\xb6\xcc\xa3\xac\xce\xd2\xd3\xc3Python'
```

这是啥？ 又 x 又 c 的！

再一看，哦，原来是十六进制字节串 (`bytes`)，`\x` 表示十六进制

接下来，你一定想转化为人类能看懂的语言，想到 `decode`：

```python
In [3]: b'\xc8\xcb\xc9\xfa\xbf\xe0\xb6\xcc\xa3\xac\xce\xd2\xd3\xc3Python'.decode()
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-3-7d0ea6148880> in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte
```

马上，一盆冷水泼头上，抛异常了。。。。。

根据提示，`UnicodeDecodeError`，这是 unicode 解码错误。

原来，`decode` 默认的编码方法：`utf-8` 

所以排除  b'\xc8\xcb\xc9\xfa\xbf\xe0\xb6\xcc\xa3\xac\xce\xd2\xd3\xc3Python' 使用 `utf-8` 的编码方式

可是，这不是四选一选择题啊，逐个排除不正确的！

编码方式几十种，不可能逐个排除吧。

那就猜吧！！！！！！！！！！！！！

**人生苦短，我用Python**

**Python， 怎忍心让你受累呢~**

尽量三行代码解决问题

**第一步，安装 chardet**  它是 char detect 的缩写。

**第二步，pip install chardet**

**第三步，出结果**

```python
In [6]: chardet.detect(b'\xc8\xcb\xc9\xfa\xbf\xe0\xb6\xcc\xa3\xac\xce\xd2\xd3\xc3Python')
Out[6]: {'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
```

编码方法：gb2312

解密字节串：

```python
In [7]: b'\xc8\xcb\xc9\xfa\xbf\xe0\xb6\xcc\xa3\xac\xce\xd2\xd3\xc3Python'.decode('gb2312')
Out[7]: '人生苦短，我用Python'
```

目前，`chardet` 包支持的检测编码几十种，如下所示：

<img src="../img/image-20200227225346560.png" width="50%"/>

