import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s1=S()
	s2=S()
	l=[]
	s=0
	for i in range(n):
		l.append(s1[i]+s2[i])
	if s1=='1'*n and s2==s1:
		print(0)
		continue
	for i in range(n):
		if l[i]=='01' or l[i]=='10':
			s+=2
		elif l[i]=='00':
			s+=1
	i=0
	di={}
	while i<n:
		if l[i]!='11':
			i+=1
			continue
		j=i+1
		while j<n and l[j]=='11':
			j+=1
		f1=(i-1>=0 and l[i-1]=='00')
		f2=(j<n and l[j]=='00')
		if f1 and di.get(i-1,-1)==-1:
			s+=1
			di[i-1]=1
			if f2 and j-i>1 and di.get(j,-1)==-1:
				s+=1
				di[j]=1
		elif f2 and di.get(j,-1)==-1:
			s+=1
			di[j]=1
		i=j
	print(s)