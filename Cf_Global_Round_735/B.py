import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=[]
	t=0
	for i in range(n):
		f=L()
		l.append(f)
	i=0
	for j in range(1,n):
		s=0
		for k in range(5):
			if l[i][k]<l[j][k]:
				s+=1
		if s<3:
			i=j
	c=0
	for p in range(n):
		s=0
		for k in range(5):
			if l[i][k]<l[p][k]:
				s+=1
		if s>=3:
			c+=1
	if c==n-1:
		print(i+1)
	else:
		print(-1)
