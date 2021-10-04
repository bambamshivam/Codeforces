import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,x=M()
	l=L()
	f=0
	p=l[:]
	l=sorted(enumerate(l),key=lambda x:x[1])
	for i in range(n):
		t=abs(l[i][0]-i)
		if t>=x or l[i][1]==p[i]:
			continue
		elif i>l[i][0] and (l[i][0]-x+t>=0 or i+x<n):
			continue
		elif i<l[i][0] and (l[i][0]+x-t<n or i-x>=0):
			continue
		else:
			f=1
	if f==1:
		print("NO")
	else:
		print("YES")