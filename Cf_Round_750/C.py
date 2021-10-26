import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S();m=math.inf
	for i in range(97,123):
		ch=chr(i);c=f=0
		l=0;r=n-1
		if s.find(ch)==-1: continue
		while l<=r:
			if s[l]==s[r]:
				l+=1;r-=1
			else:
				if s[l]==ch:
					l+=1;c+=1
				elif s[r]==ch:
					r-=1;c+=1
				else:
					f=1
					break
		if f==0: m=min(c,m)
	if m==math.inf:
		print(-1)
	else:
		print(m)