def pair(x, y):
    return tuple(zip(x, y))


r = pair((1, 2, 3), ('a', 'b', 'c'))
print(r)  # ((1, 'a'), (2, 'b'), (3, 'c'))
