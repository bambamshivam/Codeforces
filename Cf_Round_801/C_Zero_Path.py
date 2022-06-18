import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();grid=[L() for i in range(n)];c=d=0
    dp=[[[0,0] for i in range(m)] for j in range(n)]
    for i in range(n):
        c+=grid[i][0];dp[i][0]=[c,c]
    for i in range(m):
        d+=grid[0][i];dp[0][i]=[d,d]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j]=[min(dp[i-1][j][0],dp[i][j-1][0])+grid[i][j],max(dp[i-1][j][1],dp[i][j-1][1])+grid[i][j]]
    print("YES" if dp[-1][-1][0]<=0<=dp[-1][-1][1] and dp[-1][-1][1]%2==0 else "NO")