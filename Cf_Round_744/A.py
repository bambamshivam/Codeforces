import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=S()
	l=[]
	for i in range(len(s)):
		l.append(s[i])
	if l.count('B')==l.count('A')+l.count('C'):
		print("YES")
	else:
		print("NO")