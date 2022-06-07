import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();s=S();l=[0]*n
    for i in range(n):
        if s[i]=='W':l[i]=1
    p=[0]*(n+1);ans=math.inf
    for i in range(n):p[i+1]=l[i]+p[i]
    for i in range(n-k+1):ans=min(ans,p[i+k]-p[i])
    print(ans)