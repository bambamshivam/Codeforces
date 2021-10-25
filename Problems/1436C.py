import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,x,p=M()
l=0;r=n
a=[0]*n;a[p]=2
while l<r:
	m=(l+r)//2
	if m==p:
		break
	if p>m:
		a[m]=-1
		l=m+1
	else:
		a[m]=1
		r=m
l=m+1
while l<r:
	m=(l+r)//2
	a[m]=1
	r=m
p=a.count(-1);q=a.count(1);t=n-p-q-1
if p>x-1 or q>n-x:
	print(0)
else:
	g=x-1;h=n-x;ans=1
	while p>0:
		ans=(ans*g)%H
		g-=1;p-=1
	while q>0:
		ans=(ans*h)%H
		h-=1;q-=1
	while t>0:
		ans=(ans*t)%H
		t-=1
	print(ans)