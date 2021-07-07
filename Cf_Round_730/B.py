import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

for _ in range(I()):
	n=I()
	l=L()
	s=sum(l)
	t=sum(l)%n
	print(t*(n-t))