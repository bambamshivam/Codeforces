import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s1=S()
	s2=S()
	a=[s1,s2]
	if a[1][-1]=='1':
		print("NO")
		continue
	f=i=j=0
	while i<n:
		if a[j][i]=='0':
			i+=1
		elif i<n and a[1-j][i]=='0':
			j=1-j
			i+=1
		else:
			f=1
			break
	if f==1:
		print("NO")
	else:
		print("YES")