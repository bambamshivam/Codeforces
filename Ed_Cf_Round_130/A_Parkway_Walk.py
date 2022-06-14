import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();a=L();cur=m;ans=0
    for i in a:
        if i>cur:ans+=(i-cur);cur=0
        else:cur-=i
    print(ans)