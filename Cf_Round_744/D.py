import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	ans=[]
	for i in range(n):
		l[i]=[-l[i],i]
	heapq.heapify(l)
	while True:
		b=heapq.heappop(l)
		a=heapq.heappop(l)
		if a[0]<0 and b[0]<0:
			ans.append([a[1]+1,b[1]+1])
		else:
			break
		b[0]+=1
		a[0]+=1
		heapq.heappush(l,a)
		heapq.heappush(l,b)
	print(len(ans))
	for i in ans:
		print(*i)
