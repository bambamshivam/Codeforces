import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	l=L()
	l.sort()
	c=0;j=0
	for i in range(k-1,-1,-1):
		if l[i]<=j:
			break
		c+=1
		j+=n-l[i]
	print(c)