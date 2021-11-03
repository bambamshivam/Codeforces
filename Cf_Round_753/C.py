import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	if len(l)==1:
		print(l[0]);continue
	p=min(l)
	if p<0:
		l.pop(l.index(p))
		for i in range(n-1):
			l[i]-=p
	l.sort();m=min(l)
	for i in range(len(l)-1):
		m=max(l[i+1]-l[i],m)
	print(m)