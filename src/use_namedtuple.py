from collections import namedtuple

# 一般写法
lst = [(1.5, 2, 3.0), (-0.3, -1.0, 2.1), (1.3, 2.8, -2.5)]
print(lst[0][1] - lst[1][1])

# namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])  # 定义名字为Point的元祖，字段属性有x,y,z
lst = [Point(1.5, 2, 3.0), Point(-0.3, -1.0, 2.1), Point(1.3, 2.8, -2.5)]
print(lst[0].y - lst[1].y)


# 命名的元祖，写出来的代码相比第一种写法可读性更好，当属性变多时，我们甚至很难按照index方式访问元素。

# 更重要的是，当需要增加或删除一个维度时，命名元祖代码改动量比第一种要小。

# 如在属性x和y间增加一个维度k时：
Point = namedtuple('Point', ['x', 'k', 'y',  'z'])
lst = [Point(1.5, 2, 0.0, 3.0), Point(-0.3, -1.0, 0.0, 2.1),
       Point(1.3, 2.8, 0.0, -2.5)]

# 命名元素不需要重写下面代码，
print(lst[0].y - lst[1].y)

# 但是普通元祖就得如下修改：
print(lst[0][2] - lst[1][2])
