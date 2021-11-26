import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	s=S();f=0
	if int(s)%2==0:
		print(0);continue
	if int(s[0])%2==0:
		print(1);continue
	for i in s:
		if int(i)%2==0:
			f=1
	if f==1:
		print(2)
	else:
		print(-1)