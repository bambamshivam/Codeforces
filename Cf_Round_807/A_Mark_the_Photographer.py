import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,x=M();h=sorted(L());ans="YES"
    for i in range(n):
        if h[i+n]-h[i]<x:ans="NO"
    print(ans)