import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,c=input().split()
	n=int(n)
	s=S()
	if s==c*n:
		print(0)
	else:
		for i in range(n//2,n):
			if s[i]==c:
				print(1)
				print(i+1)
				break
		else:
			print(2)
			print(n,n-1)

