import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	l=L()
	a=list(enumerate(l))
	a.sort(key=lambda x:x[1])
	c=0
	for i in range(0,n*m,m):
		for j in range(i,i+m):
			for k in range(i,j):
				if a[k][0]<a[j][0] and a[k][1]<a[j][1]:
					c+=1
	print(c)
