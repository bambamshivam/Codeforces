import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	d=deque()
	d.append(l[0])
	for i in range(1,n):
		if l[i]<d[0]:
			d.appendleft(l[i])
		else:
			d.append(l[i])
	print(*d)