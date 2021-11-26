import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
	n=I()
	l=L()
	i=0;j=n-1;p=-1;f=0;a=b=0
	while i<j:
		if l[i]==l[j]:
			i+=1;j-=1
		else:
			a=l[i];b=l[j]
			break
	if a==b==0:
		print("YES");continue
	p,q=[],[]
	for i in range(n):
		if l[i]!=a:
			p.append(l[i])
		if l[i]!=b:
			q.append(l[i])
	def pal(l):
		n=len(l)
		for i in range(n//2):
			if l[i]!=l[n-i-1]:
				return False
		return True
	if pal(p) or pal(q):
		print("YES")
	else:
		print("NO")