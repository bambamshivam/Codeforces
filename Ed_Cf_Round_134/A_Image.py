import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s1=S()+S();s=set()
    for i in range(4):s.add(s1[i])
    if len(s)==4:print(3)
    elif len(s)==3:print(2)
    elif len(s)==2:print(1)
    else:print(0)