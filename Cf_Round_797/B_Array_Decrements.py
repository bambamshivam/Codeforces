import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L();f=0
    for i in range(n):
        if b[i]>a[i]:f=1;break
    if f:print("NO");continue
    m=max(a[i]-b[i] for i in range(n))
    for i in range(n):
        if a[i]-b[i]<m and b[i]!=0:f=1;break
    print("NO" if f else "YES")