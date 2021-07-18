import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	l=L()
	g,r,di=[0]*n,[0]*n,{}
	for i in range(n):
		if r[l[i]-1]==0:
			g[i]=1
			di[i]=l[i]-1
			r[l[i]-1]=1
	print(len(di))
	l1,l2=[],[]
	for i in range(n):
		if g[i]==0:
			l1.append(i)
		if r[i]==0:
			l2.append(i)
	p=len(l1)-1
	for i in range(p+1):
		if l1[i]==l2[i]:
			if i!=p:
				l1[i],l1[p]=l1[p],l1[i]
			else:
				l1[0],l1[p]=l1[p],l1[0]
	for i in range(p+1):
		di[l1[i]]=l2[i]
	if len(l1)==1 and l1[0]==l2[0]:
		di[l1[0]]=l[l1[0]]-1
		for i in range(n):
			if l[i]==l[l1[0]] and i!=l1[0]:
				di[i]=l1[0]
				break
	for i in range(n):
		print(di[i]+1,end=" ")
	print()
		



