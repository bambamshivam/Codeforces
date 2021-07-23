import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7


for _ in range(I()):
	s=input().rstrip()
	t=input().rstrip()
	n=len(s)
	m=len(t)
	f=0
	for i in range(n):
		for j in range(n-i):
			if i+j<m-j-1:
				continue
			if t==s[i:i+j+1]+s[i+2*j+1-m:i+j][::-1]:
				f=1
				break
	print("YES" if f else "NO")
