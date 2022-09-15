import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_left
for _ in range(I()):
    n=I();a=L();b=L();p=[];ans1=[];ans2=[]
    for i in range(n):ans1.append(b[bisect_left(b,a[i])]-a[i])
    for i in range(n-1):
        if b[i]<a[i+1]:p.append(i)
    p.append(n-1)
    for i in range(n):ans2.append(b[p[bisect_left(p,i)]]-a[i])
    print(*ans1);print(*ans2)