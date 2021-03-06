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
points=[list(map(int,input().split())) for i in range(n)]
#長さi*10で成り立つ、F→Tで最小
dist=[[(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2 for j in range(n)] for i in range(n)]
from collections import deque
def f(e,args):
    dp=[False]*n
    dp[0]=True
    d=deque({0})
    while len(d):
        p=d.popleft()
        for i in range(n):
            if not dp[i] and dist[p][i]<=(e*10)**2:
                d.append(i)
                dp[i]=True
    return dp[n-1]
b=binary_search(0,1,f,0,10**10,1)
print(b.value*10)