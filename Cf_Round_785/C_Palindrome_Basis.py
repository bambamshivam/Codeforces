import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n=40000;l=[i for i in range(1,n+1) if str(i)==str(i)[::-1]];dp=[0]*(n+1);dp[0]=1
for i in l:
    for j in range(i,n+1):dp[j]=(dp[j]+dp[j-i])%mod1
for _ in range(I()):print(dp[I()]%mod1)