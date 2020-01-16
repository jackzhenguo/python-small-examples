import time
import math


def excepter(f):
    i = 0
    t1 = time.time()

    def wrapper():
        try:
            f()
        except Exception as e:
            nonlocal i
            i += 1
            print(f'{e.args[0]}: {i}')
            t2 = time.time()
            if i == n:
                print(f'spending time:{round(t2-t1,2)}')
    return wrapper


n = 10  # except count


@excepter
def divide_zero_except():
    time.sleep(0.1)
    j = 1/(40-20*2)


# test zero divived except
for _ in range(n):
    divide_zero_except()


@excepter
def outof_range_except():
    a = [1, 3, 5]
    time.sleep(0.1)
    print(a[3])


# test out of range except
for _ in range(n):
    outof_range_except()
