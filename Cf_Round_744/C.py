import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m,k=M()
	l=[]
	d=[[0 for i in range(m)] for j in range(n)]
	for i in range(n):
		l.append(S())
	for i in range(n):
		for j in range(m):
			if l[i][j]=='*':
				h=1
				while i-h>=0 and j-h>=0 and j+h<m and l[i-h][j-h]=='*' and l[i-h][j+h]=='*':
					h+=1
				if h-1>=k:
					for t in range(h):
						d[i-t][j-t]=1
						d[i-t][j+t]=1
	f=0
	for i in range(n):
		for j in range(m):
			if d[i][j]==0 and l[i][j]=='*':
				f=1
				break
		if f==1:
			break
	if f==1:
		print("NO")
	else:
		print("YES")