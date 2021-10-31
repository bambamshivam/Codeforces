import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	if n%2==0:
		print("YES")
	else:
		f=0
		for i in range(n-1):
			if l[i]>=l[i+1]:
				f=1
		if f==1:
			print("YES")
		else:
			print("NO")