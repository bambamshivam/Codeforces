import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();t=sorted(L());dp=[[math.inf]*(2*n +1) for i in range(n+1)];dp[0][0]=0
    for i in range(1,n+1):
        for j in range(1,2*n+1):
            dp[i][j]=min(dp[i][j],dp[i-1][j-1]+abs(t[i-1]-j))
            dp[i-1][j]=min(dp[i-1][j],dp[i-1][j-1])
    print(min(dp[n][j] for j in range(2*n+1)))