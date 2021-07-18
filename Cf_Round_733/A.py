import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	m=0
	while n>0:
		t=n%10
		m=max(m,t)
		n=n//10
	print(m)

