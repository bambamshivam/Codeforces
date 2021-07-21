import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

t,k=M()
dp=[-1]*(100001)
s=0
l=[0]*100001
for i in range(k):
	dp[i]=pow(2,i,H)
for i in range(k,100001):
	if dp[i]==-1:
		dp[i]=((2*dp[i-1])%H + (pow(26,k,H)*(dp[i-k]%H))%H)%H
for i in range(100001):
	s=(dp[i]%H + s%H)%H
	l[i]=s
for _ in range(t):
	l1,l2=M()
	print((l[l2]-l[l1-1])%H)