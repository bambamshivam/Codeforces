import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();ans=[1]*(n+1)
    for i in range(n,0,-2):
        ans[i]=i-1;ans[i-1]=i
    if n%2:ans[1]=1
    print(*ans[1:])