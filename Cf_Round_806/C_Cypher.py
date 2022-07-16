import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    for i in range(n):
        k,s=list(S().split())
        for j in s:
            if j=='U':a[i]=(a[i]-1)%10
            else:a[i]=(a[i]+1)%10
    print(*a)