import math;import heapq;import sys;import string;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	x=L()
	y=[0]*n
	for i in range(1,n):
		y[i]=(x[i-1]^y[i-1])&(~x[i])
	print(*y)