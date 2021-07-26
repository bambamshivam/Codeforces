import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(input());M=lambda:map(int,input().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	a=[]
	m=0
	for i in range(n):
		a.append(S())
	l=[[0 for i in range(5)] for j in range(n)]
	for i in range(n):
		for j in range(len(a[i])):
			l[i][ord(a[i][j])-97]+=1
	for i in range(5):
		d=[0]*n
		si=sr=0
		for j in range(n):
			a,b=l[j][i],sum(l[j])-l[j][i]
			si+=a
			sr+=b
			d[j]=[a,b,b-a]
		d.sort(reverse=True,key=lambda x:x[2])
		for j in range(n):
			if si>sr:
				break
			si-=d[j][0]
			sr-=d[j][1]
		if si>sr:
			m=max(n-j,m)
	print(m)



