import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m,k=M();a=L()
    if k>m:print("NO")
    else:
        p=(n//k)+(n%k!=0);q=n%k;f=0;c=0
        for i in range(m):
            if a[i]>p:f=1;break
            if a[i]==p and q!=0:c+=1
        print("NO" if c>q or f==1 else "YES")