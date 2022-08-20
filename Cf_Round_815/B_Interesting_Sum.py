import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=sorted(L())
    print(max(a[-1]-a[0]+a[-2]-a[1],a[-1]-a[1]+a[-2]-a[0]))