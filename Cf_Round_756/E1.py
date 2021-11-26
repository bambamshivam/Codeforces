import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	s=S()
	n,k=M()
	a=L()
	adj=[[] for i in range(n)]
	for i in range(n-1):
		u,v=M()
		adj[u-1].append(v-1)
		adj[v-1].append(u-1)
	def bfs(i):
		q=deque()
		v=[0]*n;v[i]=1
		for j in a:
			q.append([j-1,j-1])
			v[j-1]=1
		q.append([i,i])
		while q:
			r,p=q.popleft()
			if r!=0 and p==0 and len(adj[r])==1:
				return True
			for j in adj[r]:
				if v[j]==0:
					v[j]=1
					q.append([j,p])
		return False
	print("YES" if bfs(0) else "NO")