import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,a,b=M();x=[0]+L();ans=math.inf;p=[0]*(n+1)
    for i in range(1,n+1):p[i]=p[i-1]+x[i]
    for i in range(n+1):ans=min(ans,a*x[i]+b*(p[-1]-p[i]-(n-i-1)*x[i]))
    print(ans)