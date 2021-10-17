import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M();d={}
	for i in range(m):
		a,b,c=M()
		d[b]=1
	t=0
	for i in range(1,n+1):
		if d.get(i,0)==0:
			t=i
			break
	for i in range(1,n+1):
		if i!=t:
			print(i,t)
