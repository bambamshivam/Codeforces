import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_right
for _ in range(I()):
    n,s=M();a=L();b=L();f=0;s1=set(b);d=[];ans=1;c=[]
    for i in range(n):
        if b[i]!=-1:
            if a[i]-b[i]>s:f=1;break
        else:
            c.append(a[i])
    c.sort()
    for i in range(1,n+1):
        if i not in s1:d.append(i)
    if f:print(0);continue
    n1=len(d)
    for i in range(n1):
        ans=(ans*max(bisect_right(c,d[i]+s)-i,0))%mod2
    print(ans)