import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    for i in range(n):a[i]=[a[i],i]
    a.sort();print(n-1)
    for i in range(1,n):
        print(a[i][1]+1,a[i-1][0]-(a[i][0]%a[i-1][0]))
        a[i]=[a[i][0]+a[i-1][0]-(a[i][0]%a[i-1][0]),a[i][1]]