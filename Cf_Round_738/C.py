import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	if min(l)==1:
		print(n+1,end=" ")
		for i in range(1,n+1):
			print(i,end=" ")
		print()
	else:
		i=0
		while i<n and l[i]==1:
			i+=1
		while i<n and l[i]==0:
			i+=1
		for j in range(0,i):
			print(j+1,end=" ")
		print(n+1,end=" ")
		for j in range(i,n):
			print(j+1,end=" ")
		print()
