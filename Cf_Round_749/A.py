import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
def isp(n):
	for i in range(2,n//2+1):
		if n%i==0:
			return False
	return True
for _ in range(I()):
	n=I()
	l=L()
	s=sum(l)
	a=[i for i in range(1,n+1)]
	if not isp(s):
		print(n)
		print(*a)
	else:
		for i in range(n):
			if not isp(s-l[i]):
				print(n-1)
				a.pop(i)
				break
		print(*a)