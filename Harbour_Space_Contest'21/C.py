import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

def solve(l,r,s,i):
	if (l+ (10-i+1)//2<r) or (r + (10-i)//2 +1<l):
		return i-1
	if i==10:
		return 10
	if s[i-1]=='1':
		if i%2!=0:
			return solve(l+1,r,s,i+1)
		else:
			return solve(l,r+1,s,i+1)
	elif s[i-1]=='0':
		return solve(l,r,s,i+1)
	else:
		if i%2!=0:
			return min(solve(l+1,r,s,i+1),solve(l,r,s,i+1))
		else:
			return min(solve(l,r+1,s,i+1),solve(l,r,s,i+1))

for _ in range(I()):
	s=input().rstrip()
	print(solve(0,0,s,1))

