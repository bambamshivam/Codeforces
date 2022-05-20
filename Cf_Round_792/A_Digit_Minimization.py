import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=I();s=str(s);l=list(map(int,s))
    if len(s)==2:print(l[-1])
    else:print(min(l))