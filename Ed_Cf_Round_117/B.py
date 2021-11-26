import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n,a,b=M()
	f=c1=c2=0
	for i in range(1,n+1):
		if i>a and i!=b:
			c1+=1
		if i<b and i!=a:
			c2+=1
	if c1<n//2 -1 or c2<n//2 -1:
		f=1
	if f:
		print(-1)
	else:
		d1=[];d2=[];k=n;i=1
		while i<n//2:
			if k!=a and k!=b:
				d1.append(k)
				i+=1
			k-=1
		k=1;i=1
		while i<n//2:
			if k!=a and k!=b:
				d2.append(k)
				i+=1
			k+=1
		print(*(d1+[a]+[b]+d2))