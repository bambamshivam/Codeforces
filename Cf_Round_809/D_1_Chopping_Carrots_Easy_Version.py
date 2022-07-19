import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();ans=math.inf;m=min(a)
    for i in range(m+1):
        m1=0;m2=math.inf
        for j in range(n):
            if i==0:m1=max(m1,a[j]//k);m2=min(m2,a[j]//k)
            else:
                r=math.floor(a[j]//i);r=min(r,k)
                m1=max(m1,a[j]//r);m2=min(m2,a[j]//r)
        ans=min(m1-m2,ans)
    print(ans)