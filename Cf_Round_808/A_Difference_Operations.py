import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();f=0
    for i in range(1,n):
        if a[i]%a[0]!=0:f=1
    print("NO" if f else "YES")