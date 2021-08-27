import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	l=[0]*9
	a=[]
	for i in range(9):
		l[i]=s.find(str(i+1))
	m=max(l[0],l[3],l[5],l[7],l[8])
	if m!=-1:
		a.append([1,s[m]])
	s1=s[::-1]
	t=s1.find('2')
	f=s1.find('5')
	if t!=-1 and t!=n-1:
		a.append([2,s1[t+1]+s1[t]])
	if f!=-1 and f!=n-1:
		a.append([2,s1[f+1]+s1[f]])
	if s.find('77')!=-1:
		a.append([2,77])
	if s.find('33')!=-1:
		a.append([2,33])
	if s[0]=='2':
		a.append([2,27])
	elif s[0]=='5':
		a.append([2,57])
	else:
		if s[0]=='3':
			a.append([2,33])
		else:
			a.append([2,77])
	a.sort(key=lambda x:x[0])
	print(a[0][0])
	print(a[0][1])
