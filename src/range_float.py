#以浮点数展示的等差数列
def rang(start,stop,n):
    start=float('%.2f' % start)
    stop=float('%.2f'% stop)
    n=int('%.d' % n)
    step=(stop-start)/n
    lst=[start]
    g = 0
    while g!=n:
        start=start+step
        n=n-1
        lst.append(round((start),2))
    return lst

r = rang(1,8,10)
print(r)