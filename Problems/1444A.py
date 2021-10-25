import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	p,q=M()
	if p%q!=0:
		print(p);continue
	i=2;m=1
	while i*i<=q:
		if q%i==0:
			a=i;b=q//i;c=d=p
			while c%a==0:
				c//=a
				if c%q!=0: 
					m=max(c,m)
					break
			while d%b==0:
				d//=b
				if d%q!=0:
					m=max(d,m)
					break
			m=max(c,d,m)
		i+=1
	while p%q==0:
		p//=q
	print(max(p,m))