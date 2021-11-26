import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I()
	b=L()
	p=L()
	d=[0]*n
	for i in range(n):
		d[p[i]-1]=i
	adj=[[] for i in range(n)];k=0
	for i in range(n):
		if b[i]!=i+1:
			adj[i].append(b[i]-1)
			adj[b[i]-1].append(i)
		else:
			k=i
	ans=[0]*n
	def bfs(i):
		q=deque()
		q.append(i)
		v=[0]*n
		while q:
			r=q.popleft()
			v[r]=1
			for j in adj[r]:
				if v[j]==0:
					ans[j]=d[j]-d[r]
					q.append(j)
	bfs(k);f=0
	for i in range(n):
		if i!=k and ans[i]<=0:
			f=1
	if f==1:
		print(-1);continue
	print(*ans)