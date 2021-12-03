import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I()
	a=L();c=0;p=[0]*n
	for i in range(n):
		s=0
		while a[i]%2==0:
			a[i]//=2
			c+=1
			s+=1
		p[i]=s
	m=0
	for i in range(n):
		d=0
		for j in range(n):
			if j!=i:
				d+=a[j]
		m=max(m,d+a[i]*pow(2,c))
	print(m)