import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,h=M()
	l=L()
	a=max(l)
	l.pop(l.index(a))
	b=max(l)
	t=(h//(a+b))*2
	p=h%(a+b)
	if p>0:
		t+=1
		if p>a:
			t+=1
	print(t)