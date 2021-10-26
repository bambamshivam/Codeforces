import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	a=L()
	if n%2==0:
		for i in range(0,n,2):
			a[i],a[i+1]=-a[i+1],a[i]
		print(*a)
	else:
		for i in range(0,n-3,2):
			a[i],a[i+1]=-a[i+1],a[i]
		s=a[-1]+a[-2]+a[-3]
		for i in range(n-3,n):
			if s-a[i]!=0:
				for j in range(n-3,n):
					if j!=i:
						a[j]=a[i]
				a[i]-=s
				break
		print(*a)