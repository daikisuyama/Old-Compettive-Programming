n,m=map(int,input().split())
a=[sum(list(map(int,input().split()))) for i in range(n)]
dp=[[0,0] for i in range(n)]
dp[0][0]=a[0]
for i in range(n-1):
    #食べるか食べないか
    dp[i+1][0]=max(dp[i][0],dp[i][1]+a[i+1])
    dp[i+1][1]=max(dp[i][1],dp[i][0]-a[i+1])
print(max(dp[n-1]))