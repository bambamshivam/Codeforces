import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,m1,m2=M()
adj1=[[] for i in range(n)]
adj2=[[] for i in range(n)]
for i in range(m1):
	a,b=M()
	adj1[a-1].append(b-1)
	adj1[b-1].append(a-1)
for i in range(m2):
	a,b=M()
	adj2[a-1].append(b-1)
	adj2[b-1].append(a-1)
def dfs(i,v,adj,l):
	for j in range(len(adj[i])):
		if v[adj[i][j]]==0:
			l.append(adj[i][j])
			v[adj[i][j]]=1
			dfs(adj[i][j],v,adj,l)
v1=[0]*n
cc1=[]
for i in range(n):
	if v1[i]==0:
		l1=[i]
		v1[i]=1
		dfs(i,v1,adj1,l1)
		cc1.append(l1)
v2=[0]*n
cc2=[]
for i in range(n):
	if v2[i]==0:
		l2=[i]
		v2[i]=1
		dfs(i,v2,adj2,l2)
		cc2.append(l2)
a1=[0]*n
a2=[0]*n
for i in range(len(cc1)):
	for j in cc1[i]:
		a1[j]=i
for i in range(len(cc2)):
	for j in cc2[i]:
		a2[j]=i
ans=[]
for i in range(n):
	for j in range(i+1,n):
		if a1[i]!=a1[j] and a2[i]!=a2[j]:
			t1,t2=a1[i],a2[i]
			for k in range(n):
				if a1[k]==t1:
					a1[k]=a1[j]
			for k in range(n):
				if a2[k]==t2:
					a2[k]=a2[j]
			ans.append([i+1,j+1])
print(len(ans))
for i in ans:
	print(*i)


