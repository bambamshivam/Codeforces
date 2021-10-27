import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,m=M();l=[0]*n;co=n
for i in range(m):
	a,b=M();t=min(a-1,b-1)
	l[t]+=1
	if l[t]==1: co-=1
q=I()
for i in range(q):
	p=L()
	if len(p)==3:
		a,b,c=p[0],p[1],p[2]
		if a==1:
			t=min(b-1,c-1)
			l[t]+=1
			if l[t]==1: co-=1
		else:
			t=min(b-1,c-1)
			l[t]-=1
			if l[t]==0: co+=1
	else:
		print(co)