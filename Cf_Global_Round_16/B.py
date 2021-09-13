import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=S()
	n=len(s)
	if s=='0'*n:
		print(1)
	elif s=='1'*n:
		print(0)
	else:
		i=s.find('0')
		s1=s[i+1:]
		j=s1.find('1')
		if j==-1:
			print(1)
			continue
		s2=s1[j+1:]
		k=s2.find('0')
		if k!=-1:
			print(2)
		else:
			print(1)