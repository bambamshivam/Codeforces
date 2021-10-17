import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,m=M();l=[]
for i in range(n):
	l.append(S())
dp=[0]*(m+1)
for i in range(1,n):
	for j in range(m-1):
		if l[i][j]=='X' and l[i-1][j+1]=='X':
			dp[j+1]=1
for i in range(1,m+1):
	dp[i]+=dp[i-1]
for i in range(I()):
	l,r=M()
	if dp[r-1]-dp[l-1]:
		print("NO")
	else:
		print("YES")