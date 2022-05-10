import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();ans=0
    for i in range(30,-1,-1):
        t=(1<<i);c=0
        for j in range(n):
            if a[j]&t:c+=1
        if n-c<=k:ans+=t;k-=(n-c)
    print(ans)