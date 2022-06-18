import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[L() for i in range(n)];x=y=0;ma=-math.inf
    for i in range(n):
        for j in range(m):
            if l[i][j]>ma:ma=l[i][j];x=i;y=j
    print(max(n-x,x+1)*max(m-y,y+1))