import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m,k=M()
	k-=2
	if n==1 and m==0 and k>=0:
		print("YES")
		continue
	if m>(n*(n-1))//2 or m<n-1:
		print("NO")
		continue
	if m==(n*(n-1))//2 and k>=1:
		print("YES")
		continue
	if n-1<=m<=(n*(n-1))//2 and k>=2:
		print("YES")
		continue
	print("NO")