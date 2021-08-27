import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,q=M()
	s=S()
	a=[]
	for i in range(n):
		if (s[i]=='+' and i%2==0) or (s[i]=='-' and i%2==1):
			a[i]=1
		else:
			a[i]=-1
	dp=[0]*n
	for i in range(n):
		dp[i]=dp[i-1]+a[i]
	for i in range(q):
		l,r=M()
		l-=1;r-=1
		

