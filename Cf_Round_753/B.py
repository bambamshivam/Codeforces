import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	x,n=M()
	if x%2==0:
		if n%4==0:
			print(x)
		elif n%4==1:
			print(x-n)
		elif n%4==2:
			print(x+1)
		else:
			print(x+n+1)
	else:
		if n%4==0:
			print(x)
		elif n%4==1:
			print(x+n)
		elif n%4==2:
			print(x-1)
		else:
			print(x-n-1)