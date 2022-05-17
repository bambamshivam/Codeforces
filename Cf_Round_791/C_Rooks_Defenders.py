import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
def gs(bt,i):
    s=0;i+=1
    while i>0:s+=bt[i];i-=i&(-i)
    return s
def upd(bt,n,i,v):
    i+=1
    while i<=n:bt[i]+=v;i+=i&(-i)
n,q=M();r=[0]*(n+1);c=[0]*(n+1);rc=[0]*n;cc=[0]*n
for i in range(q):
    t=L()
    if t[0]==1:
        if rc[t[1]-1]==0:upd(r,n,t[1]-1,1)
        if cc[t[2]-1]==0:upd(c,n,t[2]-1,1)
        rc[t[1]-1]+=1;cc[t[2]-1]+=1
    elif t[0]==2:
        if rc[t[1]-1]==1:upd(r,n,t[1]-1,-1)
        if cc[t[2]-1]==1:upd(c,n,t[2]-1,-1)
        rc[t[1]-1]-=1;cc[t[2]-1]-=1
    else:
        s1=gs(r,t[3]-1)-gs(r,t[1]-2)
        s2=gs(c,t[4]-1)-gs(c,t[2]-2)
        if s1!=(t[3]-t[1]+1) and s2!=(t[4]-t[2]+1):print("No")
        else:print("Yes")