import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import Counter
for _ in range(I()):
    n,k=M();a=sorted(L());c=Counter(a);d=Counter();m=0
    for i in c:
        if c[i]>=k:d[i]=d[i-1]+1
        if d[i]>d[m]:m=i
    if m==0:print(-1);continue
    print(m-d[m]+1,m)