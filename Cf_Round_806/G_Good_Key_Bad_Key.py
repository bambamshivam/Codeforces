import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();s=ans=0
    for i in range(-1,n):
        c=s
        for j in range(i+1,min(i+32,n)):
            t=a[j]
            t>>=(j-i)
            c+=t
        ans=max(ans,c)
        if i+1!=n:s+=(a[i+1]-k)
    print(ans)