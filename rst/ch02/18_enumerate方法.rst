21 枚举对象 
------------

返回一个可以枚举的对象，该对象的next()方法将返回一个元组。

.. code:: python

   In [1]: s = ["a","b","c"]
       ...: for i ,v in enumerate(s,1):
       ...:     print(i,v)
       ...:
   1 a
   2 b
   3 c

.. _header-n1379: