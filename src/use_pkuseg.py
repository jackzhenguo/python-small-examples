from pkuseg import pkuseg
from collections import Counter

mystr = """Python 语言参考 描述了 Python 语言的具体语法和语义，这份库参考则介绍了与 Python 一同发行的标准库。它还描述了通常包含在 Python 发行版中的一些可选组件。

Python 标准库非常庞大，所提供的组件涉及范围十分广泛，正如以下内容目录所显示的。这个库包含了多个内置模块 (以 C 编写)，Python 程序员必须依靠它们来实现系统级功能，例如文件 I/O，此外还有大量以 Python 编写的模块，提供了日常编程中许多问题的标准解决方案。其中有些模块经过专门设计，通过将特定平台功能抽象化为平台中立的 API 来鼓励和加强 Python 程序的可移植性。

Windows 版本的 Python 安装程序通常包含整个标准库，往往还包含许多额外组件。对于类 Unix 操作系统，Python 通常会分成一系列的软件包，因此可能需要使用操作系统所提供的包管理工具来获取部分或全部可选组件。"""

seg = pkuseg()
words = seg.cut(mystr)
top10 = Counter(words).most_common(10)
# [('的', 12), ('，', 11), ('Python', 10), ('。', 7), ('了', 5), ('包含', 4), ('组件', 4), ('标准库', 3), ('通常', 3), ('所', 3)]
print(top10)

frequency_sort = Counter(words).most_common()
with open('./data/cut_words.csv', 'w') as f:
    for line in frequency_sort:
        f.write(str(line[0])+',' + str(line[1])+"\n")

print('writing done')
