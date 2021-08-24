import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	a,b=M()
	if a>b:
		a,b=b,a
	l=[]
	n=a+b
	p,q=n//2, n//2 + n%2
	for k in range(a+b+1):
		s=max(0,k-q)
		t=min(k,p)
		x,y=(p+k-a),(k+a-q)
		if (x%2==0 and s<=x//2<=t) or (y%2==0 and s<=y//2<=t):
			l.append(k)
		"""di={}
		for i in range(s,t+1):
			di[(p+k-2*i,q+2*i-k)]=1
			di[(q+2*i-k,p+k-2*i)]=1
		if di.get((a,b),-1)!=-1:
			l.append(k)"""
	print(len(l))
	print(*l)

