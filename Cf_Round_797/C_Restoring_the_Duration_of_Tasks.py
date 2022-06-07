import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L()
    for i in range(n-1):
        if a[i+1]<b[i]:a[i+1]=b[i]
    print(*[b[i]-a[i] for i in range(n)])