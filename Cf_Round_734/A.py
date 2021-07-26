import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	x=y=n//3
	if n%3==1:
		x+=1
	elif n%3==2:
		y+=1
	print(x,y)	