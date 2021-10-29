import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	t=int(math.log(k,2))
	if n>pow(2,t):
		ans=t+1
		p=n-pow(2,t+1)
		if p>0:
			ans+=p//k + 1*(p%k!=0)
		print(ans)
	else:
		print(int(math.log(n,2)))