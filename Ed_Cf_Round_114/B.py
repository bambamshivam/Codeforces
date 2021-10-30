import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	a,b,c,m=M()
	if m>a+b+c-3:
		print("NO")
		continue
	l=[a,b,c]
	l.sort()
	t=l[2]-l[1]-l[0]
	if t>1 and m<t-1:
		print("NO")
		continue
	print("YES")

