import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I()
    if n%2==1:print(-1);continue
    n//=2
    if n==1:print(-1);continue
    print((n+2)//3,n//2)