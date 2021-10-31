import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
a=[1]*42
for i in range(1,42):
	a[i]=a[i-1]*i//math.gcd(a[i-1],i)
for _ in range(I()):
	n=I()
	l=L();f=0
	for i in range(min(n,40)):
		if l[i]%a[i+2]==0:
			f=1
			break
	if f==1:
		print("NO")
	else:
		print("YES")