import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
def ans(l,a,f):
	n=len(l)
	p1,p2=[],[]
	for i in range(n):
		if l[i]==f:
			p1.append(i)
		if a[i]==f:
			p2.append(i)
	s=0
	for i in range(len(p1)):
		s+=abs(p1[i]-p2[i])
	return s

for _ in range(I()):
	n=I()
	l=L()
	for i in range(n):
		l[i]=l[i]%2
	o=l.count(1)
	z=l.count(0)
	if abs(o-z)>1:
		print(-1)
		continue
	if o>z:
		a=[0]*n
		for i in range(0,n,2):
			a[i]=1
		print(ans(l,a,1))
	elif z>o:
		a=[1]*n
		for i in range(0,n,2):
			a[i]=0
		print(ans(l,a,0))
	else:
		a1=[0]*n
		a2=[1]*n
		for i in range(0,n,2):
			a1[i]=1
			a2[i]=0
		print(min(ans(l,a1,0),ans(l,a2,0)))

