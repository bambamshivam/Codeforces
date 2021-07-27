import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	l=[]
	for i in range(n):
		l.append(s[i])
	l.sort()
	c=0
	for i in range(n):
		if s[i]==l[i]:
			c+=1
	print(n-c)