import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=S().rstrip()
	n=len(s)
	di={}
	for i in range(n):
		if di.get(s[i],0)>=2:
			continue
		else:
			di[s[i]]=di.get(s[i],0)+1
	print(sum(list(di.values()))//2)