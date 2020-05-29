### 66 使用装饰器

from functools import wraps
import time

def print_info(f):
    """
    @para: f, 入参函数名称
    """
    @wraps(f) # 确保函数f名称等属性不发生改变
    def info():
        print('正在调用函数名称为： %s ' % (f.__name__,))
        t1 = time.time()
        f()
        t2 = time.time()
        delta = (t2 - t1)
        print('%s 函数执行时长为：%f s' % (f.__name__,delta))

    return info
        

@print_info
def f1():
    time.sleep(1.0)


@print_info
def f2():
    time.sleep(2.0)


f1()
f2()

# 输出信息如下：

# 正在调用函数名称为： f1
# f1 函数执行时长为：1.000000 s
# 正在调用函数名称为： f2
# f2 函数执行时长为：2.000000 s