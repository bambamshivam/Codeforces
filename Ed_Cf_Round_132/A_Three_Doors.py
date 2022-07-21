import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    x=I();l=L();f=0
    for i in range(3):
        if l[i]==i+1:f=1
    if l[x-1]==0:f=1
    print("NO" if f else "YES")