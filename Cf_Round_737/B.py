import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,k=M()
	l=L()
	a=list(enumerate(l))
	a.sort(key=lambda x:x[1])
	for i in range(n):
		l[a[i][0]]=[i,l[a[i][0]]]
	i=c=0
	while i<n:
		j=i+1
		while j<n and l[j][0]>0 and a[l[j][0]-1][1]==l[j-1][1]:
			j+=1
		c+=1
		i=j
	print("YES" if c<=k else "NO")