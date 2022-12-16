import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    S();l=[L(),L(),L()];s1=set();s2=set()
    for i in range(3):s1.add(l[i][0]);s2.add(l[i][1])
    if len(s1)==2 and len(s2)==2:print("NO")
    else:print("YES")