import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	r=0
	i=0
	p=0
	while r!=1:
		q=p^i
		print(q)
		sys.stdout.flush()
		r=int(input())
		if r==1:
			break
		i+=1
		p=p^q

