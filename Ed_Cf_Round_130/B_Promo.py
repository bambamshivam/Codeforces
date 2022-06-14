import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,q=M();a=sorted(L())[::-1];p=[0]*(n+1)
for i in range(n):p[i+1]=p[i]+a[i]
for i in range(q):
    x,y=M()
    if x<=y:print(p[y])
    else:print(p[x]-p[x-y])