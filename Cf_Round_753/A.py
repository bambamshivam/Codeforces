import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s1=S()
	s2=S();d={};c=0
	for i in range(len(s1)):
		d[s1[i]]=i
	for i in range(len(s2)-1):
		c+=abs(d[s2[i]]-d[s2[i+1]])
	print(c)