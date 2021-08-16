import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,m=M()
b=L()
g=L()
if max(b)>min(g):
	print(-1)
else:
	b.sort(reverse=True)
	g.sort()
	v=[1]*n
	s=sum(b)
	j=0
	for i in g:
		if v[j]>=m:
			j+=1
		if b[j]==i and v[j]==1:
			continue
		else:
			v[j]+=1
			s+=i
	for i in range(n):
		s+=(m-v[i])*b[i]
	print(s)
