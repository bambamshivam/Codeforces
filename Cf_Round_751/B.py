import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	d={};f=1;k=1;d[0]=l
	while f==1:
		d1={};f=0;p=[0]*n
		for i in l:
			d1[i]=d1.get(i,0)+1
		for i in range(n):
			p[i]=d1[l[i]]
		for i in range(n):
			if l[i]!=p[i]:
				f=1
				l=p[:]
				d[k]=l
				k+=1
				break
	k-=1
	q=I()
	for i in range(q):
		a,b=M()
		if b>k:
			b=k
		print(d[b][a-1])