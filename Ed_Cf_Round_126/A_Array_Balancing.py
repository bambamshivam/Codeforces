import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
    n=I();a=L();b=L();ans=0
    for i in range(1,n):
        if abs(a[i]-a[i-1])+abs(b[i]-b[i-1])>abs(a[i]-b[i-1])+abs(a[i-1]-b[i]):
            a[i],b[i]=b[i],a[i]
    for i in range(1,n):
        ans+=abs(a[i]-a[i-1])+abs(b[i]-b[i-1])
    print(ans)