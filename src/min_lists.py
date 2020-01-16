def min_lists(*lst):
    return min(min(*lst, key=lambda v: max(v)))


r = min_lists([1, 2, 3], [6, 7, 8], [4, 5])
print(r)  # 1
