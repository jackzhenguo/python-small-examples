import re

# 用到的正则串讲解
# \s 指匹配： [ \t\n\r\f\v]
# A|B：表示匹配A串或B串
# re.sub(pattern, newchar, string): substitue的简称，用newchar字符替代与pattern匹配的字符所有.

# title():转化为大写，例子：
# 'Hello world'.title() # 'Hello World'


# print(re.sub(r"\s|_|", "", "He llo_worl\td"))


# print(camel('some_database_field_name'))  # 'someDatabaseFieldName'
s = re.sub(r"(\s|_|-)+", " ",
           'some_database_field_name').title().replace(" ", "")  # SomeDatabaseFieldName

# 可以看到此时的第一个字符为大写，需要转化为小写
s = s[0].lower()+s[1:]  # 最终结果


# 整理以上分析得到如下代码：

def camel(s):
    s = re.sub(r"(\s|_|-)+", " ", s).title().replace(" ", "")
    return s[0].lower() + s[1:]


# 批量转化

def batch_camel(slist):
    return [camel(s) for s in slist]
