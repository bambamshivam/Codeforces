import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();c=f=0
    for i in range(n-2,-1,-1):
        if a[i+1]==0:f=1;break
        while a[i]>=a[i+1]:a[i]//=2;c+=1
    print(-1 if f else c)