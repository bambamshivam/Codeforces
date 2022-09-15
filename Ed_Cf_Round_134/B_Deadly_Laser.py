import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m,sx,sy,d=M()
    if ((sy-1)>d and (n-sx)>d) or ((sx-1)>d and (m-sy)>d):print(n+m-2)
    else:print(-1)