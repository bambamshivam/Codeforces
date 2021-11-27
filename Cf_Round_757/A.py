import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n,l,r,k=M()
	a=L()
	a.sort();c=0
	for i in range(n):
		if l<=a[i]<=r and k>=a[i]:
			k-=a[i]
			c+=1
	print(c)