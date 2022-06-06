import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();m=min(n,k);p=[0]*(n+1);ans=0
    for i in range(n):p[i+1]=p[i]+a[i]
    for i in range(n-m+1):ans=max(ans,p[i+m]-p[i])
    print(ans + (k*(k-1)//2) - ((k-m)*(k-m-1)//2))