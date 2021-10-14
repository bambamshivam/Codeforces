import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	l=L()
	a=[];m1=-1
	for i in range(m):
		p,q=input().split()
		a.append([int(p),float(q)])
	for i in range(n):
		if l[i]-1!=i:
			m1=max(i+1,m1)
	if m1==-1:
		print(1*1.0)
	else:
		s=1
		for i in range(m):
			if a[i][0]>=m1:
				s*=(1-a[i][1])
		print(1-s)
