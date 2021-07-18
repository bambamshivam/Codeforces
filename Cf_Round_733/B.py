import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	h,w=M()
	dp=[[0 for i in range(w)] for j in range(h)]
	for i in range(0,w,2):
		dp[0][i]=1
	for i in range(2,h,2):
		dp[i][w-1]=1
	s=w-1
	if dp[h-1][w-1]==1 or dp[h-2][w-1]==1:
		s=w-3
	for i in range(s,-1,-2):
		dp[h-1][i]=1
	s=h-1
	if dp[h-1][0]==1 or dp[h-1][1]==1:
		s=h-3
	for i in range(s,1,-2):
		dp[i][0]=1
	for i in range(h):
		s=""
		for j in range(w):
			s+=str(dp[i][j])
		print(s)
	print()