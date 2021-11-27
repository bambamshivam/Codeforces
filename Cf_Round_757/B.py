import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I()
	a=L()
	b=sorted(list(enumerate(a)),key=lambda x:-x[1]);ans=[0]*(n+1)
	k=1;c=-1
	for i in range(n):
		if i%2==0:
			ans[b[i][0]+1]=k
			k+=1
		else:
			ans[b[i][0]+1]=c
			c-=1
	s=0
	for i in range(1,n+1):
		s+=2*abs(ans[i])*a[i-1]
	print(s)
	print(*ans)