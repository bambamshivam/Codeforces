import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();d=[a[0]]
    for i in range(1,n):d.append(a[i]-a[i-1])
    for i in range(1,n):
        if d[i]<=0:d[0]+=d[i]
    print(sum(abs(i) for i in d))