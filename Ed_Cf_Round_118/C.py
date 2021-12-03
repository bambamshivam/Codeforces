import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n,h=M()
	a=L()
	l=0;r=10**18;ans=0
	def solve(m):
		c=0
		for i in range(n-1):
			if a[i]+m<a[i+1]:
				c+=m
			else:
				c+=a[i+1]-a[i]
		c+=m
		return c>=h
	while l<=r:
		m=(l+r)//2
		if solve(m):
			ans=m
			r=m-1
		else:
			l=m+1
	print(ans)