import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	l=L()
	p=max(n-(2*k)-1,0)
	m=-math.inf
	for i in range(p,n):
		for j in range(i+1,n):
			m=max((i+1)*(j+1) - k*(l[i] | l[j]),m)
	print(m)
