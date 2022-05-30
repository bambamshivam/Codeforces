import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();d={};mx=0
    for i in a:d[i]=d.get(i,0)+1
    while mx in d:mx+=1
    for i in range(k):
        mx+=1
        while mx in d:mx+=1
    l=sorted([i for i in set(a) if i>mx],key=lambda x:d[x]);ans=len(l)
    for i in l:
        if k>=d[i]:k-=d[i];ans-=1
    print(ans)