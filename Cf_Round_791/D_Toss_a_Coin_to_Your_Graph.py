import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
n,m,k=M();a=L();e=[]
for i in range(m):e.append(L())
adj1=[[] for i in range(n)]
for i in e:adj1[i[0]-1].append(i[1]-1)
v1=[0]*n;p1=[0]*n
print(adj1)
def dfs(r,k,v,adj,p):
    print(r,v,p)
    c=0;v[r]=1
    for j in adj[r]:
        if not v[j]:c=max(c,dfs(j,k+1,v,adj,p))
        else:c=max(c,1+p[j])
    p[r]=1+c
    return 1+c
for i in range(n):
    if v1[i]==0:
        dfs(i,1,v1,adj1,p1)
adj2=[[] for i in range(n)]
for i in e:adj2[i[1]-1].append(i[0]-1)
v2=[0]*n;p2=[0]*n
for i in range(n):
    if v2[i]==0:
        dfs(i,1,v2,adj2,p2)
print(p1,p2)
l=[[a[i],i] for i in range(n)]
l.sort(key=lambda x:x[0]);ans=-1
for i in range(n):
    t=l[i][1]
    if p1[t]+p2[t]>=k:ans=l[i][0];break
print(ans)