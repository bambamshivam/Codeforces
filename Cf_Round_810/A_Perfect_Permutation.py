import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();ans=[0]*n;p=2;q=1
    if n==1:print(1);continue
    print(*list(range(2,n+1))+[1])