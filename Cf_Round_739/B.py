import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	a,b,c=M()
	n=abs(b-a)*2
	if a<=n and b<=n and c<=n:
		if c+(n//2)>n:
			print(c-(n//2))
		else:
			print(c+(n//2))
	else:
		print(-1)