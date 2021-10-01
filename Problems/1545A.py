import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	a=sorted(l)
	d1={};d2={}
	for i in range(n):
		p=d1.get(l[i],[])
		if i%2==1:
			p.append(i)
		d1[l[i]]=p
		p=d2.get(a[i],[])
		if i%2==1:
			p.append(i)
		d2[a[i]]=p
	f=0
	for ke in d1:
		if len(d1[ke])!=len(d2[ke]):
			f=1
			break
	if f==1:
		print("NO")
	else:
		print("YES")