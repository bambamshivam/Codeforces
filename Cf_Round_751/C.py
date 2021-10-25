import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	d={}
	for i in range(31):
		c=0;p=1<<i
		for j in range(n):
			if l[j]&p: c+=1
		d[i]=c
	g=0
	for ke in d:
		g=math.gcd(g,d[ke])
	a=[]
	for i in range(1,n+1):
		if g%i==0:
			a.append(i)
	print(*a)