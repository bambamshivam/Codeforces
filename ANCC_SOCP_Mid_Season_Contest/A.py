import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000007

n=10**6
a=[1]*(n+1)
i=2
while i*i<=n:
	j=i*i
	while j<=n:
		a[j]=i*i
		j+=i*i
	i+=1
for _ in range(I()):
	n=I()
	l=L()
	di={}
	for i in range(n):
		l[i]//=a[l[i]]
		di[l[i]]=di.get(l[i],0)+1
	print(max(list(di.values())))
