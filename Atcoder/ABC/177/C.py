n=int(input())
a=list(map(int,input().split()))
x=sum(a)
y=sum([(a[i])**2 for i in range(n)])
print(((x**2-y)//2)%(10**9+7))