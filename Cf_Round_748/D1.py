import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	t=min(l);g=0
	if t==max(l):
		print(-1);continue
	for i in range(n):
		g=math.gcd(g,l[i]-t)
	print(g)