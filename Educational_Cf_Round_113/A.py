import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	f=0
	for i in range(n):
		for j in range(i+1,n):
			s1=s[i:j+1]
			if s1.count('a')==s1.count('b'):
				print(i+1,j+1)
				f=1
				break
		if f==1:
			break
	if f==0:
		print(-1,-1)