import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();p=L();ans=0
    for i in range(k,n):
        if 1<=p[i]<=k:ans+=1
    print(ans)