import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
l=[]
i=1;c=0
while c<=1000:
	if i%3!=0 and str(i)[-1]!='3':
		l.append(i)
		c+=1
	i+=1
for _ in range(I()):
	k=I()
	print(l[k-1])