import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=input()
	t=['00','25','50','75']
	m=20
	for i in t:
		p=1
		for j in range(len(n)-1,-1,-1):
			if n[j]==i[p]:
				p-=1
			if p==-1:
				m=min(m,len(n)-j-3)
				break
	print(m)