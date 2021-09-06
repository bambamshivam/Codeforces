import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n=I()
l=L()
dp=[0]*n
o=c=0
for i in range(n-1,-1,-1):
	if i%2==0:
		o+=l[i]
	else:
		c+=l[i]
	dp[i]=[o,c]
ans=0
for i in range(0,n,2):
	j=i+1
	if j<n and l[i]>=l[j] and dp[j][1]-dp[j][0]<=l[i]:
		s=dp[i+1][1]-dp[i+1][0]
		if s<=0:
			continue
		c=0
		while s>c:
			if j%2==1:
				c+=l[j]
			else:
				s+=l[j]
			j+=1
		if s==c:
			if j+1<n and dp[j+1][1]-dp[j+1][0]>=l[j]:
				ans+=1
		ans+=s-l[i+1]
print(ans)
