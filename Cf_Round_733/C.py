import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	y=L()
	l=L()
	n1=len(l)
	y.sort()
	l.sort()
	k=n- n//4
	j=n-k
	i=n-k-1
	s=sum(y[j:])
	t=sum(l[j:])
	while s<t:
		n+=1
		if n%4==0:
			if j<n1:
				s+=(100-y[j])
				j+=1
		else:
			s+=100
			if i>=0:
				t+=l[i]
				i-=1
	print(n-n1)


