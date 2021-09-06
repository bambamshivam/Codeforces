import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

def solve(x,n,b):
	if x==b:
		print(n+1)
	elif b^x==a:
		print(n+3)
	else:
		print(n+2)

for _ in range(I()):
	a,b=M()
	n=a-1
	r=n%4
	if r==0:
		solve(n,n,b)
	elif r==1:
		solve(1,n,b)
	elif r==2:
		solve(n+1,n,b)
	else:
		solve(0,n,b)