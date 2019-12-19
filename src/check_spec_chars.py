import re

# 检查字符串是否包含除了数字和字母（含大小写）之外的特殊符号。例如字符串learnpython110*7%%99hello，如果作为此函数的参数，则返回True


def has_spec_chars(mystr):
    pat = re.compile(r'\W+')
    return pat.search(mystr) != None


r = has_spec_chars('learnpython110*7%%99hello')
print(r)
