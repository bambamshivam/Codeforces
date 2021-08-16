import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	p=0
	cur=max(l)
	while max(l)!=min(l):
		p=cur
		i=min(l.index(max(l)),l.index(min(l)))
		j=max(l.index(max(l)),l.index(min(l)))
		for k in range(j-i+1):
			l[i+k]=l[j-k]&l[i+k]
		cur=max(l)
	print(max(l))