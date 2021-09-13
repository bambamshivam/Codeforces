import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	l=L()
	a=list(enumerate(l))
	a.sort(key=lambda x:(x[1],-x[0]))
	p=[]
	for i in range(m):
		p.append([a[i][0],i,a[i][1]])
	p.sort()
	t=[-1]*m
	i=s=0
	while i<m:
		t[p[i][1]]=i
		c=0
		for j in range(p[i][1]):
			if t[j]!=-1:
				c+=1
		s+=c
		i+=1
	print(s)