from collections.abc import Iterator
#编写一个迭代器，通过循环语句，实现对某个正整数的依次递减1，直到0.
class Descend(Iterator):
    def __init__(self,N):
        self.N=N
        self.a=0
    def __next__(self):
        while self.a<self.N:
            self.N-=1
            return self.N
        raise StopIteration
    
descend_iter=Descend(10)

try:
    for i in descend_iter:
        print(i)
except StopIteration as e:
    print('迭代结束')
    
