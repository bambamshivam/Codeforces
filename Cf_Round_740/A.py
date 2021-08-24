import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	a=sorted(l)
	k=0
	while True:
		f=0
		for i in range(n):
			if l[i]!=a[i]:
				f=1
				break
		if f==1:
			k+=1
		else:
			break
		if k%2==1:
			for i in range(0,n-2,2):
				if l[i]>l[i+1]:
					l[i],l[i+1]=l[i+1],l[i]
		else:
			for i in range(1,n-1,2):
				if l[i]>l[i+1]:
					l[i],l[i+1]=l[i+1],l[i]
		
	print(k)
