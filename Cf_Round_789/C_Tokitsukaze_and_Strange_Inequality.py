import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();p=L();l=[0]*n;ans=0
    for i in range(1,n-2):
        c=0
        for j in range(n-2,i,-1):
            if p[i-1]<p[j]:l[j]+=1
            if p[j+1]<p[i]:c+=1
            ans+=c*l[j]
    print(ans)