import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	l=[S() for i in range(n)]
	print(sum(i.count('1') for i in l)*3)
	for i in range(n):
		for j in range(m):
			if l[i][j]=='1':
				a=i+2 if i<n-1 else i
				b=j+2 if j<m-1 else j
				print(i+1,j+1,i+1,b,a,b)
				print(i+1,j+1,a,j+1,a,b)
				print(i+1,j+1,i+1,b,a,j+1)