import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    a,b=M()
    if a>b:print('01'*b+'0'*(a-b))
    else:print('10'*a+'1'*(b-a))