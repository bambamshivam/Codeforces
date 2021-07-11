import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=input()
	n,k=M()
	po=L()
	t=L()
	h=math.inf
	a=[h]*n
	l,r=[0]*n,[0]*n
	for i in range(k):
		a[po[i]-1]=t[i]
	p=h
	for i in range(n):
		p=min(p+1,a[i])
		l[i]=p
	p=h
	for i in range(n-1,-1,-1):
		p=min(p+1,a[i])
		r[i]=p
	for i in range(n):
		l[i]=min(l[i],r[i])
	print(*l)
