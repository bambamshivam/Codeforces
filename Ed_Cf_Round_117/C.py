import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	k,x=M();s=0
	l=0;r=2*k-1
	while l<=r:
		m=(l+r)//2
		if m<=k:
			t=m*(m+1)//2
		else:
			p=2*k-1-m
			t=k*k - p*(p+1)//2
		if t>x:
			r=m-1
		elif t<=x:
			s=m
			l=m+1
	if (s<=k and x>s*(s+1)//2) or (s>k and x>k*k - (2*k-s-1)*(2*k-s)//2):
		print(min(2*k-1,s+1))
	else:
		print(s)