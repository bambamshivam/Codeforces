import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import deque
n=I();adj=[[] for i in range(n)]
for i in range(n-1):
    p,q=M()
    adj[p-1].append(q-1)
    adj[q-1].append(p-1)
p=[-1]*n;d=[0]*n
q=deque([0]);v=[0]*n
while q:
    r=q.popleft()
    v[r]=1
    for j in adj[r]:
        if v[j]==0:
            q.append(j);d[j]=d[r]+1;p[j]=r
q=I()
for i in range(q):
    k=I()
    a=L();y=a[:]
    f=0;z=[]
    j=0;m=0;s=set()
    for i in a:
        if d[i-1]>m:m=d[i-1];j=i-1
    while j not in s:
        s.add(j);z.append(j);j=p[j]
        if j==-1:break
    b=[]
    for i in a:
        if i-1 not in s:b.append(i)
    a=b[:]
    if len(a)==0:print("YES");continue
    j=0;m=0;s1=set();x=0
    for i in a:
        if d[i-1]>m:m=d[i-1];j=i-1
    while j not in s and p[j]!=-1:
        s1.add(j);j=p[j]
    for t in range(len(z)-1,-1,-1):
        if z[t]==j:x=1
        if x==1:s1.add(z[t])
    for i in y:
        if i-1 not in s1:f=1;break
    print("NO" if f else "YES")