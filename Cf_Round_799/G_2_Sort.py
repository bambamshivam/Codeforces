import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();l=[0]*(n-1);ans=0
    for i in range(n-1):
        if a[i+1]*2>a[i]:l[i]=1
    p=[0]*(n)
    for i in range(n-1):p[i+1]=p[i]+l[i]
    for i in range(n-k):
        if p[i+k]-p[i]==k:ans+=1
    print(ans)