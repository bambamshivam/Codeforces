import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
n,d=M()
p=[-1]*(n+1);c=0
def find(x):
	if p[x]<0: return x
	return find(p[x])
for i in range(d):
	x,y=M()
	if find(x)==find(y):
		c+=1
	else:
		p[find(x)]+=p[find(y)]
		p[find(y)]=find(x)
	ans=0;a=sorted(p)
	for j in range(c+1):
		if a[j]<0:
			ans+=a[j]
	print(-1-ans)