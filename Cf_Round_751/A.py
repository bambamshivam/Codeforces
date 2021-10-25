import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=S();a="";f=0;m=math.inf
	for i in s:
		if ord(i)<m:
			m=ord(i);ch=i
	for i in s:
		if i==ch and f==0:
			f=1
		else:
			a+=i
	print(ch,a)