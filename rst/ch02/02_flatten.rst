=================
2.2 嵌套数组完全展开
=================

嵌套数组完全展开

.. code-block:: python

   from collections.abc import *

   def flatten(input_arr, output_arr=None):
   if output_arr is None:
	