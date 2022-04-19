import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M()
    if (n==1 and m>2) or (m==1 and n>2):print(-1);continue
    t=min(n,m);ans=2*t-2;p=max(n,m)-t
    if p%2==0:
        ans+=2*p
    else:
        ans+=2*p-1
    print(ans)