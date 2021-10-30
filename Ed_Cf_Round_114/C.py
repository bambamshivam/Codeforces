import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n=I()
l=L()
l.sort()
s=sum(l)
m=I()
for i in range(m):
	a,b=M()
	c=0
	i=bisect_left(l,a)
	if i==n:
		print(a-l[-1]+max(0,b-s+l[-1]))
	elif i==0:
		print(max(0,b-s+l[i]))
	else:
		if abs(l[i-1]-a)+max(0,b-s+l[i-1])<max(0,b-s+l[i]):
			print(abs(l[i-1]-a)+max(0,b-s+l[i-1]))
		else:
			print(max(0,b-s+l[i]))