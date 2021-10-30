import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=[];a=[]
	for i in range(n):
		l.append(L())
	for i in range(5):
		s="";c=0
		for j in range(n):
			s+=str(l[j][i])
			c+=l[j][i]
		a.append((int(s,2),c))
	f=0
	p=int('1'*n,2)
	for i in range(5):
		for j in range(i+1,5):
			if a[i][0] | a[j][0]==p and a[i][1]>=n//2 and a[j][1]>=n//2 :
				f=1
				break
	if f==1:
		print("YES")
	else:
		print("NO")