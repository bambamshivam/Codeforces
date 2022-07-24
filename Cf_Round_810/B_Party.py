import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,m=M();a=L();l=[L() for i in range(m)];ans=math.inf;d=[0]*n
    for i in range(m):d[l[i][0]-1]+=1;d[l[i][1]-1]+=1
    if m%2==0:print(0);continue
    for i in range(n):
        if d[i]%2:ans=min(ans,a[i])
    for i in range(m):
        if d[l[i][0]-1]%2==0 and d[l[i][1]-1]%2==0:ans=min(ans,a[l[i][0]-1]+a[l[i][1]-1])
    print(ans)