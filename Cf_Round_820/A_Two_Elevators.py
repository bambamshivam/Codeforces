import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    a,b,c=M()
    if abs(a-1)<abs(b-c)+abs(c-1):print(1)
    elif abs(a-1)>abs(b-c)+abs(c-1):print(2)
    else:print(3)