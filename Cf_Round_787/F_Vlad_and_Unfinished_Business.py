import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import deque
for _ in range(I()):
    S();n,k=M();x,y=M();x-=1;y-=1;a=L();e=[]
    for i in range(n-1):e.append(L())
    adj=[[] for i in range(n)]
    for i in e:adj[i[0]-1].append(i[1]-1);adj[i[1]-1].append(i[0]-1)
    q=deque([x]);p=[0]*n;v=[0]*n;p[x]=x
    while q:
        r=q.popleft();v[r]=1
        for j in adj[r]:
            if v[j]==0:q.append(j);p[j]=r
    l=[y];ans=0
    for i in a:
        if i-1!=y:l.append(i-1)
    v=[0]*n;l=list(set(l));l1=[y]
    for i in l:
        if i!=y:l1.append(i)
    l=l1[:];ans=0
    for i in l:
        cur=i;c=0
        while v[cur]==0:
            c+=1;v[cur]=1;cur=p[cur]
        if i==y:ans+=c-1
        else:ans+=2*c
    print(ans)