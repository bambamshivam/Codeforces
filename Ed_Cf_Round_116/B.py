import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	t=1;c=0
	while t<k:
		t*=2
		c+=1
	p=n-t
	if p>0:
		c+=p//k
		if p%k>0:
			c+=1
	print(c)