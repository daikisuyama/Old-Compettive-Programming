#https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
mod=10000
n,k=map(int,input().split())
pasta=[-1]*n
for i in range(k):
    a,b=map(int,input().split())
    pasta[a-1]=b-1
dp=[[[0]*2 for i in range(3)] for j in range(n)]
if pasta[0]==-1:
    for i in range(3):
        dp[0][i][0]=1
else:
    dp[0][pasta[0]][0]=1
#今どこ見てるか
for i in range(n-1):
    if pasta[i+1]!=-1:
        #今変わるのはどこか(pasta[i]のみ)
        for j in range(3):
            if j==pasta[i+1]:
                #それ自身を選ぶ場合
                dp[i+1][j][1]+=dp[i][j][0]
                #異なるところにいく場合
                for k in range(3):
                    if k!=j:
                        dp[i+1][j][0]+=sum(dp[i][k])
    else:
        for j in range(3):
            #それ自身を選ぶ場合
            dp[i+1][j][1]+=dp[i][j][0]
            #異なるところにいく場合
            for k in range(3):
                if k!=j:
                    dp[i+1][j][0]+=sum(dp[i][k])
ans=0
for i in range(3):
    ans+=sum(dp[n-1][i])
print(ans%mod)