import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	if 1<=s.count('2')<=2:
		print("NO")
		continue
	p=[0]*n
	a=[[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			if a[i][j]!=0:
				continue
			if i==j:
				a[i][j]='X'
			elif (s[i]==s[j] and s[i]=='1') or s[i]!=s[j]:
				a[i][j]='='
				a[j][i]='='
			else:
				if p[i]==0:
					a[i][j]='+'
					p[i]=1
					a[j][i]='-'
				else:
					a[i][j]='-'
					a[j][i]='+'
					p[j]=1
	print("YES")
	for i in a:
		s1=""
		for j in i:
			s1+=j
		print(s1)