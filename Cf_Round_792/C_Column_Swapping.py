import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();l=[L() for i in range(n)];d=[[] for i in range(n)];f=0
    for i in range(n):
        a=sorted(l[i])
        for j in range(m):
            if l[i][j]!=a[j]:d[i].append(j)
    for i in d:
        if len(i)>2:f=1;break
    b=[i for i in d if len(i)==2]
    for i in range(len(b)-1):
        if b[i]!=b[i+1]:f=1;break
    if f:print(-1);continue
    if len(b)==0:print(1,1);continue
    p,q=b[0][0],b[0][1]
    for i in range(n):
        if len(d[i])==0 and l[i][p]!=l[i][q]:f=1;break
    if f:print(-1);continue
    print(b[0][0]+1,b[0][1]+1)