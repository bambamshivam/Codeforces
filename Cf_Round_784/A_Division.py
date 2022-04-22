import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    r=I();ans=4
    if r>=1900:ans=1
    elif 1600<=r<=1899:ans=2
    elif 1400<=r<=1599:ans=3
    print("Division",ans)