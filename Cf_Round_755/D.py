import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
	n=I()
	print('?',1,n);sys.stdout.flush()
	s=I()
	l=1;r=n;i=1
	while l<=r:
		m=(l+r)//2
		print('?',m,n);sys.stdout.flush()
		t=I()
		if t<s:
			r=m-1
		else:
			if t==s: i=m
			l=m+1
	print('?',i+1,n);sys.stdout.flush()
	j=s-I()+i+1
	c=s-((j-i)*(j-i-1)//2)
	k=round((2*j - 1 + (math.sqrt(1+8*c)))/2)
	print('!',i,j,k);sys.stdout.flush()