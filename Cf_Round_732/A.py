import math;import heapq;import string;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	a=L()
	b=L()
	if sum(a)!=sum(b):
		print(-1)
	else:
		l=[]
		if n==1 and a[0]!=b[0]:
			print(-1)
		else:
			i=0
			j=0
			while i<n and j<n:
				while i<n and a[i]<=b[i]:
					i+=1
				while j<n and a[j]>=b[j]:
					j+=1
				if i>=n or j>=n:
					break
				l.append([i+1,j+1])
				a[i]-=1
				a[j]+=1
			print(len(l))
			for i in l:
				print(*i)



