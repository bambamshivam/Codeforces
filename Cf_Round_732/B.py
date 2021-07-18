import math;import heapq;import string;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	l,a=[],[]
	for i in range(n):
		l.append(input())
	for i in range(n-1):
		a.append(input())
	dp1=[0 for i in range(m)]
	dp2=[0 for i in range(m)]
	s=""
	for i in range(m):
		for j in range(n):
			dp1[i]+=ord(l[j][i])
			if j!=n-1:
				dp2[i]+=ord(a[j][i])
	for i in range(m):
		s+=chr(dp1[i]-dp2[i])
	print(s)
	sys.stdout.flush()
