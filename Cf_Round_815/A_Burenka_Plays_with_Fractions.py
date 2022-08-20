import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    a,b,c,d=M()
    if [a,c].count(0)==0:
        if (a*d)==(b*c):print(0)
        elif (a*d)%(b*c)==0 or (b*c)%(a*d)==0:print(1)
        else:print(2)
    elif [a,c].count(0)==1:print(1)
    else:print(0)