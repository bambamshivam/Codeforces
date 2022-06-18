import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
import heapq
n,m=M();adj=[[] for i in range(n)];d=[0]*n;vis=[0]*n;dist=[m+1]*n;dist[-1]=0;h=[[0,n-1]];heapq.heapify(h)
for i in range(m):u,v=M();adj[v-1].append(u-1);d[u-1]+=1
while h:
    r=heapq.heappop(h)[1]
    if vis[r]:continue
    vis[r]=1
    for j in adj[r]:
        if d[j]+dist[r]<dist[j]:dist[j]=d[j]+dist[r];heapq.heappush(h,[dist[j],j])
        d[j]-=1
print(dist[0])