import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(int(input())):
	l=list(map(int,input().split()))
	t=max(l)
	ans=[]
	if l.count(t)>1:
		for i in range(3):
			if l[i]==t:
				ans.append(1)
			else:
				ans.append(t-l[i]+1)
	else:
		for i in range(3):
			if l[i]==t:
				ans.append(0)
			else:
				ans.append(t-l[i]+1)
	print(*ans)