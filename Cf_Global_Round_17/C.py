import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I();a=[]
	for i in range(n):
		a.append(L())
	l=1;r=n;ans=0
	while l<=r:
		m=(l+r)//2
		i=0
		for j in range(n):
			if a[j][0]>=m-i-1 and a[j][1]>=i:
				i+=1
		if i>=m:
			ans=m
			l=m+1
		else:
			r=m-1
	print(ans)