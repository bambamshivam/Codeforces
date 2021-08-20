import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	k=I()
	m=int(math.sqrt(k))
	if m*m==k:
		print(m,1)
	elif k-m*m<=m+1:
		print(k-m*m,m+1)
	else:
		print(m+1,m*m+2*m+2-k)

