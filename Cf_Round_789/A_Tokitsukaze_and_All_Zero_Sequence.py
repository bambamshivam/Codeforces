import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    if a.count(0)>0:print(n-a.count(0));continue
    if len(set(a))!=n:print(n);continue
    print(n+1)