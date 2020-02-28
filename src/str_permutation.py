from collections import defaultdict


def is_permutation(str1: str, str2: str) -> bool:
    if str1 is None or str2 is None:
        return False
    if len(str1) != len(str2):
        return False
    unq_s1 = defaultdict(int)
    unq_s2 = defaultdict(int)
    for c1 in unq_s1:
        unq_s1[c1] += 1
    for c2 in unq_s2:
        unq_s2[c2] += 1

    return unq_s1 == unq_s2


r = is_permutation('nice', 'cine')
print(r)  # True

r = is_permutation('', '')
print(r)  # True

r = is_permutation('', None)
print(r)  # False

r = is_permutation('work', 'woo')
print(r)  # False
