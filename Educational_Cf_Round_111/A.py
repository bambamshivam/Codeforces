import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	c,s=1,0
	while n>0:
		if n>=c:
			n-=c
			s+=1
			c+=2
		else:
			s+=1
			n=0
	print(s)

