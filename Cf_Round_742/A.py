import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	a=""
	i=0
	while i<n:
		if s[i]=='L' or s[i]=='R':
			a+=s[i]+s[i+1]
			i+=2
		elif s[i]=='U':
			a+='D'
			i+=1
		else:
			a+='U'
			i+=1
	print(a)