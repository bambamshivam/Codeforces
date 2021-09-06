import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

def solve(i,s,ans,a):
	if i>=len(s):
		return ans
	else:
		p=int(s[i])+a[i]
		if i+2<len(s) and p+10<=18:
			f=0
			if i+2<len(a):
				a[i+2]+=1
				f=1
			elif i+1<len(a):
				a.append(1)
				f=2
			else:
				a.append(0)
				a.append(1)
				f=3
			c=(2*p+12)
			x=solve(i+1,s,ans*c,a)
			if f==1:
				a[i+2]-=1
			if f==2:
				a.pop()
			elif f==3:
				a.pop()
				a.pop()
		else:
			

for _ in range(I()):
	n=I()
	s=str(n)[::-1]
	t=len(s)
	i=0
	while i<len(a):
		if 
		for j in range(i+1,t):
