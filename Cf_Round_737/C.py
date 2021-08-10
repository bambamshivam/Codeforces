import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	s=0
	if n%2==1:
		s=pow(pow(2,n-1,H)+1,k,H)
	else:
		d=(pow(2,n-1,H)-1)%H
		p=(pow(2,n,H)*pow(d,-1,H))%H
		z=pow(d,k-1,H)
		m=pow(p,k,H)-1
		q=p-1
		s=(m%H)*(pow(q,-1,H))*(z)
		s+=pow(d,k,H)
	print(s%H)
