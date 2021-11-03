import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	s=S()
	a=list(zip(s,l))
	a.sort();f=0
	for i in range(n):
		if a[i][0]=='B' and a[i][1]<i+1:
			f=1;break
		if a[i][0]=='R' and a[i][1]>i+1:
			f=1;break
	if f:
		print("NO")
	else: print("YES")