import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,k=M()
s=S()
l=[]
for i in range(1,n+1):
	s1=s[:i]
	t=k//i +1
	s2=s1*t
	s2=s2[:k]
	l.append(s2)
print(min(l))