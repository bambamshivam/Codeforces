import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
mod=998244353
for _ in range(I()):
	n=I()
	l=L()
	m=max(l)
	f=k=1
	t=l.count(m-1)
	for i in range(n):
		f=(f%mod * (i+1)%mod)%mod
		if i!=t:
			k=(k%mod * (i+1)%mod)%mod
	if m==min(l) or l.count(m)>1:
		print(f%mod)
		continue
	if m-1 not in l:
		print(0)
		continue
	print((f-k)%mod)