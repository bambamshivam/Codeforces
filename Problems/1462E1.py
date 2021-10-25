import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	a=[0]*(n+2)
	for i in l:
		a[i-1]+=1
	b=a[:-2]
	for i in range(1,n+2):
		a[i]+=a[i-1]
	s=0
	for i in range(n):
		if b[i]>0:
			q=a[i+2]-a[i]
			s+=b[i]*math.comb(q,2) + math.comb(b[i],2)*q + math.comb(b[i],3)
	print(s)