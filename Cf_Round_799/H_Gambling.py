import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
for _ in range(I()):
    n=I();a=L();d=defaultdict(list);m=0;p=q=r=0
    for i in range(n):d[str(a[i])].append(i)
    for t in d:
        l=d[t]
        i=j=0;n1=len(l)
        while j<n1:
            while j<n1 and 2*(j-i+1)-(l[j]-l[i]+1)>0:
                if 2*(j-i+1)-(l[j]-l[i]+1)>m:
                    m=2*(j-i+1)-(l[j]-l[i]+1);p=l[i];q=l[j];r=t
                j+=1
            i=j
    print(r,p+1,q+1)