def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    #約数の小さい順にソートしたい場合
    #divisors.sort()
    #約数の大きい順にソートしたい場合
    #divisors.sort(reverse=True)
    return divisors
s,p=map(int,input().split())
for i in make_divisors(p):
    if i+p//i==s:
        print("Yes")
        break
else:
    print("No")