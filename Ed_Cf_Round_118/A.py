import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	x1,p1=M()
	x2,p2=M()
	if len(str(x1))+p1>len(str(x2))+p2:
		print('>')
	elif len(str(x1))+p1<len(str(x2))+p2:
		print('<')
	else:
		t=abs(p1-p2)
		if len(str(x1))<=len(str(x2)):
			x1=int(str(x1)+'0'*t)
		else:
			x2=int(str(x2)+'0'*t)
		if x1<x2:
			print('<')
		elif x1>x2:
			print('>')
		else:
			print('=')