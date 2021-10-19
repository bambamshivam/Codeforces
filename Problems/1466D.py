import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	w=L();d=[0]*n
	for i in range(n-1):
		a,b=M()
		d[a-1]+=1
		d[b-1]+=1
	a=[]
	for i in range(n):
		for j in range(d[i]-1):
			a.append(w[i])
	a.sort(reverse=True)
	ans=sum(w);l=[]
	for i in a:
		l.append(ans)
		ans+=i
	l.append(ans)
	print(*l)