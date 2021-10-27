import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s1=S()
	s2=S();d={};c=0
	for i in range(n):
		if s2[i]=='1':
			if i-1>=0 and s1[i-1]=='1' and d.get(i-1,0)==0:
				c+=1;d[i-1]=1
			elif s1[i]=='0':
				c+=1
			elif i+1<n and s1[i+1]=='1' and d.get(i+1,0)==0:
				c+=1;d[i+1]=1
	print(c)
