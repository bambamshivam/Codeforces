import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	x,y=M()
	d=abs(x)+abs(y)
	if d%2==1:
		print(-1,-1)
	else:
		if x%2==0:
			print(x//2,y//2)
		else:
			print(x//2,y//2 +1)