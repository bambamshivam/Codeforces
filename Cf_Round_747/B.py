import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	l=[]
	t=1
	while k>0:
		t=int(math.ceil(math.log(k+1,2)))-1
		l.append(t)
		k-=(pow(2,t))
	s=0
	for i in l:
		s=(s+pow(n,i,H))%H
	print(s)