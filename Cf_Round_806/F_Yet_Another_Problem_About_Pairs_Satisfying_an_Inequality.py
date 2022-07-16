import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();l=[0]*n;ans=0
    for i in range(n):
        if a[i]<i+1:l[i]=1
    p=[0]*(n+1)
    for i in range(n):p[i+1]=p[i]+l[i]
    for i in range(n):
        if l[i]==1 and 1<=a[i]<=n:
            ans+=p[a[i]-1]
    print(ans)