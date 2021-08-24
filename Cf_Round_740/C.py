import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	a=[]
	for i in range(n):
		m,*l=M()
		for j in range(m):
			l[j]=l[j]-j+1
		a.append([max(l),m])
	a.sort()
	m=a[0][0]
	s=a[0][1]
	for i in range(1,n):
		if a[i][0]>=s+m:
			m+=(a[i][0]-s-m)
		s+=a[i][1]
	print(m)

