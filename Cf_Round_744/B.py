import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	a=l[:]
	a.sort()
	ans=[]
	for i in range(n):
		if a[i]!=l[i]:
			t=l[i:].index(a[i])
			t+=i
			ans.append([i+1,n,t-i])
			k=i
			p=l[:]
			for j in range(t,n):
				p[k]=l[j]
				k+=1
			for j in range(i,t):
				p[k]=l[j]
				k+=1
			l=p[:]
	print(len(ans))
	for i in ans:
		print(*i)
