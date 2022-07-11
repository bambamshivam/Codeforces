import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
for _ in range(I()):
    n=I();d={};f=0;l=[];s1=set()
    for i in range(n):
        p,q=M();l.append([p,q]);s1.add(p);s1.add(q)
        if p==q:f=1
        d[p]=d.get(p,0)+1
        d[q]=d.get(q,0)+1
    for i in d:
        if d[i]>2:f=1;break
    if f:print("NO");continue
    s=set()
    adj=defaultdict(set)
    for i in l:
        adj[i[0]].add(i[1])
        adj[i[1]].add(i[0])
    for i in s1:
        if i in s:continue
        j=i;c=0
        while j not in s:
            c+=1;s.add(j)
            j1=adj[j].pop()
            if j1 in s and len(adj[j])>0:
                j1=adj[j].pop()
            j=j1
        if c%2==1:f=1;break
    print("NO" if f else "YES")