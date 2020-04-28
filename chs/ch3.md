### 三、Python文件、日期和多线程

Python文件IO操作涉及文件读写操作，获取文件`后缀名`，修改后缀名，获取文件修改时间，`压缩`文件，`加密`文件等操作。

Python日期章节，由表示大日期的`calendar`, `date`模块，逐渐过渡到表示时间刻度更小的模块：`datetime`, `time`模块，按照此逻辑展开。

Python`多线程`希望透过5个小例子，帮助你对多线程模型编程本质有些更清晰的认识。

一共总结最常用的`26`个关于文件和时间处理模块的例子。

#### 116 获取后缀名

```python
import os
file_ext = os.path.splitext('./data/py/test.py')
front,ext = file_ext
In [5]: front
Out[5]: './data/py/test'

In [6]: ext
Out[6]: '.py'
```

#### 117 文件读操作

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

#### 118  文件写操作

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

#### 119 路径中的文件名

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

#### 120 批量修改文件后缀

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



#### 121 xls批量转换成xlsx

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



#### 122 定制文件不同行


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



#### 123 获取指定后缀名的文件

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


#### 124 批量获取文件修改时间

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
    

#### 125 批量压缩文件


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

#### 126 32位加密

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

#### 127 年的日历图

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

#### 128 判断是否为闰年

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

#### 129 月的日历图

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

#### 130 月有几天

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



#### 131 月第一天

```python
from datetime import date
mydate = date.today()
month_first_day = date(mydate.year, mydate.month, 1)
print(f"当月第一天:{month_first_day}\n")

```

打印结果：

```python
# 当月第一天:2019-12-01

```



#### 131 月最后一天

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



#### 132 获取当前时间

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



#### 133 字符时间转时间

```python
from time import strptime

# parse str time to struct time
struct_time = strptime('2019-12-22 10:10:08', "%Y-%m-%d %H:%M:%S")
print(struct_time) # struct_time类型就是time中的一个类

# time.struct_time(tm_year=2019, tm_mon=12, tm_mday=22, tm_hour=10, tm_min=10, tm_sec=8, tm_wday=6, tm_yday=356, tm_isdst=-1)

```



#### 134 时间转字符时间

```python
from time import strftime, strptime, localtime

In [2]: print(localtime()) #这是输入的时间
Out[2]: time.struct_time(tm_year=2019, tm_mon=12, tm_mday=22, tm_hour=18, tm_min=24, tm_sec=56, tm_wday=6, tm_yday=356, tm_isdst=0)

print(strftime("%m-%d-%Y %H:%M:%S", localtime()))  # 转化为定制的格式
# 这是字符串表示的时间：   12-22-2019 18:26:21

```



#### 135 默认启动主线程

一般的，程序默认执行只在一个线程，这个线程称为主线程，例子演示如下：

导入线程相关的模块 `threading`:

```python
import threading
```

threading的类方法 `current_thread()`返回当前线程：

```python
t = threading.current_thread()
print(t) # <_MainThread(MainThread, started 139908235814720)>
```

所以，验证了程序默认是在`MainThead`中执行。

`t.getName()`获得这个线程的名字，其他常用方法，`getName()`获得线程`id`,`isAlive()`判断线程是否存活等。

```python
print(t.getName()) # MainThread
print(t.ident) # 139908235814720
print(t.isAlive()) # True
```

以上这些仅是介绍多线程的`背景知识`，因为到目前为止，我们有且仅有一个"干活"的主线程

#### 136 创建线程

创建一个线程：

```python
my_thread = threading.Thread()
```

创建一个名称为`my_thread`的线程：

```python
my_thread = threading.Thread(name='my_thread')
```

创建线程的目的是告诉它帮助我们做些什么，做些什么通过参数`target`传入，参数类型为`callable`，函数就是可调用的：

```python
def print_i(i):
    print('打印i:%d'%(i,))
my_thread = threading.Thread(target=print_i,args=(1,))

```

`my_thread`线程已经全副武装，但是我们得按下发射按钮，启动start()，它才开始真正起飞。

```python
my_thread().start()

```

打印结果如下，其中`args`指定函数`print_i`需要的参数i，类型为元祖。

```python
打印i:1

```

至此，多线程相关的核心知识点，已经总结完毕。但是，仅仅知道这些，还不够！光纸上谈兵，当然远远不够。

接下来，聊聊应用多线程编程，最本质的一些东西。

**3 交替获得CPU时间片**

为了更好解释，假定计算机是单核的，尽管对于`cpython`，这个假定有些多余。

开辟3个线程，装到`threads`中:

```python
import time
from datetime import datetime
import threading


def print_time():
    for _ in range(5): # 在每个线程中打印5次
        time.sleep(0.1) # 模拟打印前的相关处理逻辑
        print('当前线程%s,打印结束时间为:%s'%(threading.current_thread().getName(),datetime.today()))


threads = [threading.Thread(name='t%d'%(i,),target=print_time) for i in range(3)]

```

启动3个线程：

```python
[t.start() for t in threads]

```

打印结果如下，`t0`,`t1`,`t2`三个线程，根据操作系统的调度算法，轮询获得CPU时间片，注意观察，`t2`线程可能被连续调度，从而获得时间片。

```python
当前线程t0,打印结束时间为:2020-01-12 02:27:15.705235
当前线程t1,打印结束时间为:2020-01-12 02:27:15.705402
当前线程t2,打印结束时间为:2020-01-12 02:27:15.705687
当前线程t0,打印结束时间为:2020-01-12 02:27:15.805767
当前线程t1,打印结束时间为:2020-01-12 02:27:15.805886
当前线程t2,打印结束时间为:2020-01-12 02:27:15.806044
当前线程t0,打印结束时间为:2020-01-12 02:27:15.906200
当前线程t2,打印结束时间为:2020-01-12 02:27:15.906320
当前线程t1,打印结束时间为:2020-01-12 02:27:15.906433
当前线程t0,打印结束时间为:2020-01-12 02:27:16.006581
当前线程t1,打印结束时间为:2020-01-12 02:27:16.006766
当前线程t2,打印结束时间为:2020-01-12 02:27:16.007006
当前线程t2,打印结束时间为:2020-01-12 02:27:16.107564
当前线程t0,打印结束时间为:2020-01-12 02:27:16.107290
当前线程t1,打印结束时间为:2020-01-12 02:27:16.107741

```

#### 137 多线程抢夺同一个变量

多线程编程，存在抢夺同一个变量的问题。

比如下面例子，创建的10个线程同时竞争全局变量`a`:
​

```python
import threading


a = 0
def add1():
    global a    
    a += 1
    print('%s  adds a to 1: %d'%(threading.current_thread().getName(),a))
    
threads = [threading.Thread(name='t%d'%(i,),target=add1) for i in range(10)]
[t.start() for t in threads]

```

执行结果：

```python
t0  adds a to 1: 1
t1  adds a to 1: 2
t2  adds a to 1: 3
t3  adds a to 1: 4
t4  adds a to 1: 5
t5  adds a to 1: 6
t6  adds a to 1: 7
t7  adds a to 1: 8
t8  adds a to 1: 9
t9  adds a to 1: 10

```

结果一切正常，每个线程执行一次，把`a`的值加1，最后`a` 变为10，一切正常。

运行上面代码十几遍，一切也都正常。

所以，我们能下结论：这段代码是线程安全的吗？

NO！

多线程中，只要存在同时读取和修改一个全局变量的情况，如果不采取其他措施，就一定不是线程安全的。

尽管，有时，某些情况的资源竞争，暴露出问题的概率`极低极低`：

本例中，如果线程0 在修改a后，其他某些线程还是get到的是没有修改前的值，就会暴露问题。



但是在本例中，`a = a + 1`这种修改操作，花费的时间太短了，短到我们无法想象。所以，线程间轮询执行时，都能get到最新的a值。所以，暴露问题的概率就变得微乎其微。

#### 138 代码稍作改动，叫问题暴露出来

只要弄明白问题暴露的原因，叫问题出现还是不困难的。

想象数据库的写入操作，一般需要耗费我们可以感知的时间。

为了模拟这个写入动作，简化期间，我们只需要延长修改变量`a`的时间，问题很容易就会还原出来。

```python
import threading
import time


a = 0
def add1():
    global a    
    tmp = a + 1
    time.sleep(0.2) # 延时0.2秒，模拟写入所需时间
    a = tmp
    print('%s  adds a to 1: %d'%(threading.current_thread().getName(),a))
    
threads = [threading.Thread(name='t%d'%(i,),target=add1) for i in range(10)]
[t.start() for t in threads]

```

重新运行代码，只需一次，问题立马完全暴露，结果如下：

```python
t0  adds a to 1: 1
t1  adds a to 1: 1
t2  adds a to 1: 1
t3  adds a to 1: 1
t4  adds a to 1: 1
t5  adds a to 1: 1
t7  adds a to 1: 1
t6  adds a to 1: 1
t8  adds a to 1: 1
t9  adds a to 1: 1

```

看到，10个线程全部运行后，`a`的值只相当于一个线程执行的结果。

下面分析，为什么会出现上面的结果：

这是一个很有说服力的例子，因为在修改a前，有0.2秒的休眠时间，某个线程延时后，CPU立即分配计算资源给其他线程。直到分配给所有线程后，根据结果反映出，0.2秒的休眠时长还没耗尽，这样每个线程get到的a值都是0，所以才出现上面的结果。



以上最核心的三行代码：

```python
tmp = a + 1
time.sleep(0.2) # 延时0.2秒，模拟写入所需时间
a = tmp

```

#### 139 加上一把锁，避免以上情况出现

知道问题出现的原因后，要想修复问题，也没那么复杂。

通过python中提供的锁机制，某段代码只能单线程执行时，上锁，其他线程等待，直到释放锁后，其他线程再争锁，执行代码，释放锁，重复以上。

创建一把锁`locka`:

```python
import threading
import time


locka = threading.Lock()

```

通过 `locka.acquire()` 获得锁，通过`locka.release()`释放锁，它们之间的这些代码，只能单线程执行。

```python
a = 0
def add1():
    global a    
    try:
        locka.acquire() # 获得锁
        tmp = a + 1
        time.sleep(0.2) # 延时0.2秒，模拟写入所需时间
        a = tmp
    finally:
        locka.release() # 释放锁
    print('%s  adds a to 1: %d'%(threading.current_thread().getName(),a))
    
threads = [threading.Thread(name='t%d'%(i,),target=add1) for i in range(10)]
[t.start() for t in threads]

```

执行结果如下：

```python
t0  adds a to 1: 1
t1  adds a to 1: 2
t2  adds a to 1: 3
t3  adds a to 1: 4
t4  adds a to 1: 5
t5  adds a to 1: 6
t6  adds a to 1: 7
t7  adds a to 1: 8
t8  adds a to 1: 9
t9  adds a to 1: 10

```

一起正常，其实这已经是单线程顺序执行了，就本例子而言，已经失去多线程的价值，并且还带来了因为线程创建开销，浪费时间的副作用。

程序中只有一把锁，通过 `try...finally`还能确保不发生死锁。但是，当程序中启用多把锁，还是很容易发生死锁。

注意使用场合，避免死锁，是我们在使用多线程开发时需要注意的一些问题。

#### 140 1 分钟掌握 time 模块

time 模块提供时间相关的类和函数

记住一个类：`struct_time`，9 个整数组成的元组

记住下面 5 个最常用函数

首先导入`time`模块

```python
import time

```

**1 此时此刻时间浮点数**

```python
In [58]: seconds = time.time()
In [60]: seconds
Out[60]: 1582341559.0950701

```

**2 时间数组**

```python
In [61]: local_time = time.localtime(seconds)

In [62]: local_time
Out[62]: time.struct_time(tm_year=2020, tm_mon=2, tm_mday=22, tm_hour=11, tm_min=19, tm_sec=19, tm_wday=5, tm_yday=53, tm_isdst=0)

```

**3 时间字符串**

`time.asctime` 语义： `as convert time`

```python
In [63]: str_time = time.asctime(local_time)

In [64]: str_time
Out[64]: 'Sat Feb 22 11:19:19 2020'

```

**4 格式化时间字符串**

`time.strftime` 语义： `string format time`

```python
In [65]: format_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)

In [66]: format_time
Out[66]: '2020-02-22 11:19:19'

```

**5 字符时间转时间数组**

```python
In [68]: str_to_struct = time.strptime(format_time,'%Y-%m-%d %H:%M:%S')

In [69]: str_to_struct
Out[69]: time.struct_time(tm_year=2020, tm_mon=2, tm_mday=22, tm_hour=11, tm_min=19, tm_sec=19, tm_wday=5, tm_yday=53, tm_isdst=-1)

```

最后再记住常用字符串格式

**常用字符串格式**

%m：月

%M: 分钟

```markdown
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
```

#### 141 4G 内存处理 10G 大小的文件

4G 内存处理 10G 大小的文件，单机怎么做？

下面的讨论基于的假定：可以单独处理一行数据，行间数据相关性为零。

方法一：

仅使用 Python 内置模板，逐行读取到内存。

使用 yield，好处是解耦读取操作和处理操作：

```python
def python_read(filename):
    with open(filename,'r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                return
            yield line
```

以上每次读取一行，逐行迭代，逐行处理数据

```python
if __name__ == '__main__':
    g = python_read('./data/movies.dat')
    for c in g:
        print(c)
        # process c
```

方法二：

方法一有缺点，逐行读入，频繁的 IO 操作拖累处理效率。是否有一次 IO ，读取多行的方法？

`pandas` 包 `read_csv` 函数，参数有 38 个之多，功能非常强大。

关于单机处理大文件，`read_csv` 的 `chunksize` 参数能做到，设置为 `5`， 意味着一次读取 5 行。

```python
def pandas_read(filename,sep=',',chunksize=5):
    reader = pd.read_csv(filename,sep,chunksize=chunksize)
    while True:
        try:
            yield reader.get_chunk()
        except StopIteration:
            print('---Done---')
            break
```

使用如同方法一：

```python
if __name__ == '__main__':
    g = pandas_read('./data/movies.dat',sep="::")
    for c in g:
        print(c)
        # process c
```

以上就是单机处理大文件的两个方法，推荐使用方法二，更加灵活。除了工作中会用到，面试中也有时被问到。