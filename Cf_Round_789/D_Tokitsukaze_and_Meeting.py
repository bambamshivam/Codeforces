import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();s=S();r=[0]*(1+max(n,m));c=[0]*(1+max(n,m));d=0;l=-math.inf;ans=[]
    for i in range(n*m):
        if s[i]=='1':
            l=i
            if c[i%m]==0:d+=1;c[i%m]=1
        if i-l<m:r[i%m]+=1
        ans.append(r[i%m]+d)
    print(*ans)