import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,m=M()
s=S()
p=n%3;q=n//3
l=["abc","acb","bac","bca","cab","cba"]
for i in range(6):
	l[i]=l[i]*q + l[i][:p]
	a=[0]*(n+1)
	for j in range(1,n+1):
		a[j]=a[j-1]
		if s[j-1]!=l[i][j-1]:
			a[j]=a[j-1]+1
	l[i]=a

for i in range(m):
	t,r=M()
	m=n+1
	for j in range(6):
		m=min(m,l[j][r]-l[j][t-1])
	print(m)