import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_left
for _ in range(I()):
    n,q=M();a=sorted(L())[::-1];p=[0]*(n+1)
    for i in range(n):p[i+1]=p[i]+a[i]
    for i in range(q):
        x=I()
        if p[-1]<x:print(-1);continue
        i=bisect_left(p,x)
        print(i)