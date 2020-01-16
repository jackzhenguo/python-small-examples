def search_n(s, c, n):
    size = 0
    for i, x in enumerate(s):
        if x == c:
            size += 1
        if size == n:
            return i
    return -1



print(search_n("fdasadfadf", "a", 3))# 结果为7，正确
print(search_n("fdasadfadf", "a", 30))# 结果为-1，正确
