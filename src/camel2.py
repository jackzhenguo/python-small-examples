import re

# 另一种写法


def hump_str(string="a_-_b", pattern='\s|_|-'):
    _ = re.compile(pattern).sub('', string.title())
    return _.replace(_[0], _[0].lower())


print(hump_str())
