import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    S();n,k=M();a=L();d1={};d2={}
    for i in range(n):
        p=str(a[i])
        if p not in d1:d1[p]=i
    for i in range(n-1,-1,-1):
        p=str(a[i])
        if p not in d2:d2[p]=i
    for i in range(k):
        p,q=M();p=str(p);q=str(q)
        if p not in d1 or q not in d2:print("NO");continue
        print("YES" if d1[p]<=d2[q] else "NO")