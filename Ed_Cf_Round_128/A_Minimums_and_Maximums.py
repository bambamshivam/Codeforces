import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    l1,r1,l2,r2=M()
    if max(l1,l2)<=min(r1,r2):print(max(l1,l2));continue
    print(l1+l2)