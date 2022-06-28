import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();ans=0
    for i in range(1,n-1):
        if a[i]>a[i-1]+a[i+1]:ans+=1
    if k>1:print(ans)
    else:
        n-=2
        print(n//2 + n%2)