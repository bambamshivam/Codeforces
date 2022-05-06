import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=0;r=1000000000;ans=0
    while l<=r:
        i=(l+r)//2
        p=i*2//3;q=p//2;s=(p*(p+1)//2)*2 + (q*(q+1)//2)*4
        if (i+1)*2//3==p:s-=(2*p)
        if s>=n:ans=i;r=i-1
        else:l=i+1
    print(ans)