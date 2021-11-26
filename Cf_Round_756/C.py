import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I()
	l=L()
	if l[0]!=n and l[-1]!=n:
		print(-1);continue
	if l[0]==n:
		a=[l[0]]+l[1:][::-1]
	else:
		a=l[:-1][::-1]+[l[-1]]
	print(*a)