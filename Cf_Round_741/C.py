import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	t=s.find('0')
	if t==-1:
		print(1,n//2,n//2+1,2*(n//2))
	elif t<n//2:
		print(t+1,n,t+2,n)
	else:
		print(1,t+1,1,t)