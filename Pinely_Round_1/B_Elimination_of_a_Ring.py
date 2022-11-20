import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    if len(a)==1:print(1);continue
    if len(a)==2:print(2);continue
    if len(a)==3:print(3);continue
    k=-1
    for i in range(n):
        if a[i]!=a[(i+2)%n]:k=(i+1)%n;break
    print((n//2)+1 if k==-1 else n)