===============================
1.4 不使用if和else做一个计算器
===============================

.. code:: python

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

