import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for i in range(I()):
	n=I()
	s='('*n + ')'*(n-1)
	for i in range(1,n+1):
		s1=s[:i]+')'+s[i:]
		print(s1)
	
