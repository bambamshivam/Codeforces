import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=sorted(a);f=0
    for i in range(n%2,n-1,2):
        if min(a[i],a[i+1])!=b[i] or max(a[i],a[i+1])!=b[i+1]:f=1;break
    print("NO" if f else "YES")