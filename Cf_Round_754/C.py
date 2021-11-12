import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353;sys.setrecursionlimit(10000000)
for _ in range(I()):
	n=I()
	s=S()
	if 'aa' in s:
		print(2);continue
	if 'aba' in s or 'aca' in s:
		print(3);continue
	if 'abca' in s or 'acba' in s:
		print(4);continue
	if 'abbacca' in s or 'accabba' in s:
		print(7);continue
	print(-1)