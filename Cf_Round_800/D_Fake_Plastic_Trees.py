import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import deque
for _ in range(I()):
    n=I();p=L();l=[L() for i in range(n)];ran=[0]*n;adj=[[] for i in range(n)]
    for i in range(n-1):adj[p[i]-1].append(i+1)
    ans=sum(1 for i in range(1,n) if len(adj[i])==0);q=deque([[0,0]]);b=[0]*n
    while q:
        r,c=q.popleft()
        for j in adj[r]:q.append([j,c+1]);b[j]=c+1
    m=max(b);d=[[] for i in range(m+1)]
    for i in range(n):d[b[i]].append(i)
    for i in range(m,0,-1):
        s1=set()
        for j in d[i]:
            p1=p[j-1]-1;ran[p1]+=l[j][1];s1.add(p1)
        for p1 in s1:
            if ran[p1]<l[p1][0]:ans+=1
            else:l[p1]=[l[p1][0],min(l[p1][1],ran[p1])]
    print(ans)