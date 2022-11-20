import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,a,b=M()
    if a+b>=n:
        if (a!=n or b!=n):print("No")
        else:print("Yes")
        continue
    if n-a-b<2:print("No");continue
    print("Yes")