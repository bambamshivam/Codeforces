import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

for _ in range(I()):
	s=S()
	t=S()
	n=len(s)
	m=len(t)
	if m>n:
		print("NO")
		continue
	if s==t or t=="":
		print("YES")
		continue
	i=n-1
	j=m-1
	while i>=0 and j>=0:
		if s[i]!=t[j]:
			i-=2
		else:
			i-=1
			j-=1
	print("YES" if j<0 else "NO")
	
