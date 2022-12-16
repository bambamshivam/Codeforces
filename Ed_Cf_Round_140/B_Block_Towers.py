import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for i in range(I()):
    n=I();a=L();a=[a[0]]+sorted(a[1:])
    for i in range(1,n):
        if a[i]<=a[0]:continue
        a[0]+=(a[i]-a[0]+1)//2
    print(a[0])