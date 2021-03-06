#二分探索
from operator import floordiv,truediv,truth,not_
from math import log
'''
domain:= 定義域が整数(0)or実数(1)
searchtype:= T→Fで最大値(0)かF→Tで最小値(1)か
f:= boolを返す関数(単調性が必要)(答えでtrueを返すように) 
l,r:= 探索範囲(l,rはsearchtypeの条件を満たすように)
eps:= 誤差(整数なら1,実数なら誤差指定による)
args:= fの引数(iterable)…f(i,args)という形にして展開する必要がある
'''
#答えはvalueに格納
class binary_search:
    def __init__(self,domain,searchtype,f,l,r,eps,args=None):
        self.domain=domain
        self.searchtype=searchtype
        self.f=f
        self.args=args
        self.l,self.r=l,r
        self.iter=int(log((r-l)/eps,2.0))+5
        self.op1=[floordiv,truediv][domain]
        self.op2=[not_,truth][searchtype]
        self.value=self.calc()
    def calc(self):
        for _ in range(self.iter):
            diff=self.op1(self.r-self.l,2)
            bisection=self.l+diff
            if self.op2(self.f(bisection,self.args)):
                self.r=bisection
            else:
                self.l=bisection
        return [self.l,self.r][self.searchtype]

n=int(input())
#i秒目、F→T、Tの最小
def g(i):
    return i*(i+1)//2
def f(i,args):
    return g(i)>=n
#0でF、10**10でT
b=binary_search(0,1,f,0,10**10,1)
if g(b.value)==n:
    print("YES")
    print(b.value)
else:
    print("NO")