import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m,k=M();a=L();p=[];q=[];n1=n;m1=m;l=r=0
    for i in a:p.append(i//n);q.append(i//m)
    p.sort();q.sort()
    for i in p[::-1]:
        if m1==1 and l<3:break
        if i<=1:continue
        if m1<=i:m1=0;l=max(l,i)
        else:m1-=i;l=max(l,i)
    for i in q[::-1]:
        if n1==1 and r<3:break
        if i<=1:continue
        if n1<=i:n1=0;r=max(r,i)
        else:n1-=i;r=max(r,i)
    if m1==0 or n1==0:print("Yes")
    else:print("No")