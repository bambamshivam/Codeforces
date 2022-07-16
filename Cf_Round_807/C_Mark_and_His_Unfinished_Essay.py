import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from bisect import bisect_left
for _ in range(I()):
    n,c,q=M();s=S();a=[len(s)];l=[]
    for i in range(c):
        l.append(L())
        a.append(l[-1][1]-l[-1][0]+1+a[-1])
    for i in range(q):
        k=I()
        while k>n:
            t=bisect_left(a,k)
            k=l[t-1][0]+(k-a[t-1])-1
        print(s[k-1])
