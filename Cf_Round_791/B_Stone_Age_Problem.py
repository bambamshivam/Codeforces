import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,q=M();a=L();b=[1]*n;cur=-1;s=set(list(range(1,n+1)));ans=sum(a)
for i in range(q):
    t=L()
    if t[0]==1:
        if t[1] in s:ans+=(t[2]-a[t[1]-1]);a[t[1]-1]=t[2]
        else:ans+=(t[2]-cur);a[t[1]-1]=t[2];s.add(t[1])
    else:cur=t[1];s=set();ans=t[1]*n
    print(ans)