import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[L() for i in range(n)];ans=0
    for i in range(n):
        for j in range(m):
            s=l[i][j]
            p,q=i,j;s-=l[p][q]
            while p>=0 and q>=0:
                s+=l[p][q];p-=1;q-=1
            p,q=i,j;s-=l[p][q]
            while p>=0 and q<m:
                s+=l[p][q];p-=1;q+=1
            p,q=i,j;s-=l[p][q]
            while p<n and q>=0:
                s+=l[p][q];p+=1;q-=1
            p,q=i,j;s-=l[p][q]
            while p<n and q<m:
                s+=l[p][q];p+=1;q+=1
            ans=max(ans,s)
    print(ans)