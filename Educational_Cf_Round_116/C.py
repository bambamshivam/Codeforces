import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M();k+=1
	l=L();s="";i=0
	while i<n and k>0:
		if i+1<n:
			a='9'*(l[i+1]-l[i])
			if k>=int(a):
				k-=int(a)
				s+=a
			else:
				s+=str(k)[::-1]
				break
			i+=1
		else:
			s+=str(k)[::-1]
			break
	print(s[::-1])