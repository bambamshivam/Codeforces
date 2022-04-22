import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();d={};f=1
    for i in a:d[i]=d.get(i,0)+1
    for i in d:
        if d[i]>=3:print(i);f=0;break
    if f:print(-1)