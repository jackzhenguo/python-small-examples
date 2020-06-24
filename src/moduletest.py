def main():
    print('do something in module',__name__)


if __name__ == '__main__':
    print('executed module from the command line')
    main()


def merge(left, right):
    i = 0
    j = 0
    temp = []
    while i <= len(left) - 1 and j <= len(right) - 1:
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp += left[i:] + right[j:]
    return temp

print(merge([1,3,4],[2,3,3]))    


def merge_sort(lst):
    #
    #
    #
    return lst_sorted