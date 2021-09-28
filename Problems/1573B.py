import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	a=L()
	b=L()
	m=ans=n
	l=[0]*(2*n+1)
	for i in range(n):
		l[a[i]]=i
		l[b[i]]=i
	for i in range(2*n,0,-1):
		if i%2==0:
			m=min(l[i],m)
		else:
			ans=min(ans,l[i]+m)
	print(ans)