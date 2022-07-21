import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,m=M();a=L();p=[0]*n;q=[0]*n
for i in range(1,n):p[i]=p[i-1]+max(a[i-1]-a[i],0)
for i in range(n-2,-1,-1):q[i]=q[i+1]+max(a[i+1]-a[i],0)
for i in range(m):
    s,t=M()
    if s<t:print(p[t-1]-p[s-1])
    else:print(q[t-1]-q[s-1])