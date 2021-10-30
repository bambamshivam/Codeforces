import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=[]
	for i in range(n):
		l.append(L())
	d1={};d2={}
	for i in range(n):
		d1[l[i][0]]=d1.get(l[i][0],0)+1
		d2[l[i][1]]=d2.get(l[i][1],0)+1
	p=0
	for i in range(n):
		p+=(d1[l[i][0]]-1)*(d2[l[i][1]]-1)
	print(n*(n-1)*(n-2)//6  -  p)