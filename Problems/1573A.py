import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	c=0
	for i in range(n-2,-1,-1):
		if s[i]!='0':
			c+=int(s[i])+1
	c+=int(s[-1])
	print(c)