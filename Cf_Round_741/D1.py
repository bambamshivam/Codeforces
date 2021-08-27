import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,q=M()
	s=S()
	a=[0]*n
	for i in range(n):
		if (s[i]=='+' and i%2==0) or (s[i]=='-' and i%2==1):
			a[i]=1
		else:
			a[i]=-1
	dp=[0]*(n+1)
	for i in range(n):
		dp[i+1]=dp[i]+a[i]
	for i in range(q):
		l,r=M()
		if dp[r]-dp[l-1]==0:
			print(0)
		elif (r-l+1)%2==1:
			print(1)
		else:
			print(2)



