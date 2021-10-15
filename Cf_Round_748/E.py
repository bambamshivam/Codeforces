import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=S()
	n,k=M()
	adj=[[] for i in range(n)]
	d=[0]*n
	for i in range(n-1):
		a,b=M()
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
		d[a-1]+=1
		d[b-1]+=1
	ans=n
	q=deque()
	for i in range(n):
		if d[i]==1:
			q.append(i)
	for p in range(k):
		if len(q)==0 or ans==1:
			ans=0
			break
		for i in range(len(q)):
			t=q.popleft()
			d[t]=0
			ans-=1
			for j in adj[t]:
				d[j]-=1
				if d[j]==1:
					q.append(j)
	print(ans)