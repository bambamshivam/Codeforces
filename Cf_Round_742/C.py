import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=str(n)
	s1,s2="0","0"
	for i in range(len(s)):
		if i%2==0:
			s1+=s[i]
		else:
			s2+=s[i]
	print((int(s1)+1)*(int(s2)+1) - 2)