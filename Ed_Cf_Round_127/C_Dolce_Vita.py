import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_left
for _ in range(I()):
    n,x=M();a=sorted(L());p=[0]*(n+1)
    for i in range(n):p[i+1]=a[i]+p[i]
    i=n;ans=0
    while 1:
        while i>=1 and p[i]>x:i-=1
        if i<1:break
        ans+=((x-p[i])//i + 1)
        i-=1
    print(ans)