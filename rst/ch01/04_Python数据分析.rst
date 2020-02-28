4 Python数据分析
----------------

Python非常适合做数值计算、数据分析，一行代码完成数据透视：

.. code:: python

   pd.pivot_table(df, index=['Manager', 'Rep'], values=['Price'], aggfunc=np.sum)

.. _header-n1303: