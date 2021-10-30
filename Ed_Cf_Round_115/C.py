import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	k=sum(l)/len(l)
	d=sum(l)-((n-2)*k);di={}
	for i in range(n):
		di[l[i]]=di.get(l[i],0)+1
	s=0
	for i in range(n):
		if l[i]!=d-l[i]:
			s+=di[l[i]]*di.get(d-l[i],0)
			di[l[i]]=0
			di[d-l[i]]=0
		else:
			s+=((di[l[i]]-1)*di[l[i]])//2
			di[l[i]]=0
	print(s)