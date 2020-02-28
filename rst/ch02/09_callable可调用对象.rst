11 是否可调用 
--------------

判断对象是否可被调用，能被调用的对象就是一个\ ``callable``
对象，比如函数 ``str``, ``int`` 等都是可被调用的，但是例子\ **4**
中\ ``xiaoming``\ 实例是不可被调用的：

.. code:: python

   In [1]: callable(str)
   Out[1]: True

   In [2]: callable(int)
   Out[2]: True

   In [3]: xiaoming
   Out[3]: id = 001, name = xiaoming

   In [4]: callable(xiaoming)
   Out[4]: False

如果想让\ ``xiaoming``\ 能被调用 xiaoming(),
需要重写\ ``Student``\ 类的\ ``__call__``\ 方法：

.. code:: python

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

.. _header-n1349: