import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();print((((2*n*(n+1)*(2*n+1)//6) - (n*(n+1)//2))*2022)%mod1)