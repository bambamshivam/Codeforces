import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for t in range(I()):
	n,m=M()
	l=[];lx=ly=0;c=[0,1,0,-1,0]
	for i in range(n):
		l.append(list(S()))
		if 'L' in l[-1]:
			lx=i;ly=l[-1].index('L')
	def solve(i,j):
		p=0
		for k in range(4):
			p+=(0<=i+c[k]<n and 0<=j+c[k+1]<m) and (l[i+c[k]][j+c[k+1]]=='.')
		return p
	q=deque()
	q.append((lx,ly))
	while q:
		r=q.popleft()
		for k in range(4):
			x,y=r[0]+c[k],r[1]+c[k+1]
			if (0<=x<n and 0<=y<m) and l[x][y]=='.' and solve(x,y)<=1:
				l[x][y]='+'
				q.append((x,y))
	for i in l:
		print(''.join(i))