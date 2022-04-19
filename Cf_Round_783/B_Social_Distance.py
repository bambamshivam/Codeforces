import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();a=sorted(L())[::-1];i=1;c=1+2*a[0]
    while i<n-1:
        c+=a[i]+a[i+1]+2
        i+=2
    if i==n-1:
        c+=1
    else:
        c-=a[-1]
    if c<=m:print("YES")
    else:print("NO")