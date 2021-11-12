import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
	n=I()
	s=S();l=[];f=0
	t=s.count('1')
	for i in range(n-t):
		if s[i]=='1':
			l.append(i+1)
	for i in range(n-t,n):
		if s[i]=='0':
			f=1
			l.append(i+1)
	if f==0:
		print(0);continue
	print(1)
	print(len(l),*l)