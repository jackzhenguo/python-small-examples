4 ascii展示对象 
----------------

调用对象的\ **repr**\ ()
方法，获得该方法的返回值，如下例子返回值为字符串

.. code:: python

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

.. _header-n1326: