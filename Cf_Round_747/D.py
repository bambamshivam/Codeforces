import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	adj=[[] for i in range(n+m+5)]
	col=[-1 for i in range(n+m+5)]
	fake=n+1
	for k in range(m):
		i,j,c=input().split()
		i,j=int(i),int(j)
		if c=="crewmate":
			adj[i].append((fake,1))
			adj[fake].append((i,1))
			adj[j].append((fake,1))
			adj[fake].append((j,1))
			fake+=1
		else:
			adj[i].append((j,1))
			adj[j].append((i,1))
	c=[0]*2
	flag=[0]
	def bfs(t):
		q=deque()
		q.append(t)
		while q:
			i=q.popleft()
			if i<=n:
				c[col[i]]+=1
			for j in range(len(adj[i])):
				if col[adj[i][j][0]]==-1:
					col[adj[i][j][0]]=col[i]^adj[i][j][1]
					q.append(adj[i][j][0])
				elif col[adj[i][j][0]]!=col[i]^adj[i][j][1]:
					flag[0]=1
	ans=0
	for i in range(1,n+1):
		if col[i]==-1:
			col[i]=0
			c[0]=0;c[1]=0
			bfs(i)
			ans+=max(c[0],c[1])
	if flag[0]:
		ans=-1
	print(ans)