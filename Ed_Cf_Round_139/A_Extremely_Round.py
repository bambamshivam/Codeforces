import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();ans=0
    s=str(n)
    if s[0]=='1':print(9*(len(s)-1) + 1)
    else:print(9*(len(s)-1) + (int(s[0])))