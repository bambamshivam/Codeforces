import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    x,y=M();t=y//x;s=set();c=0
    if y%x!=0:print(0,0);continue
    print(1,y//x)