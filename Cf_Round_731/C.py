import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=S()
	k,n,m=M()
	a=L()
	b=L()
	i=j=f=0
	l=[]
	while i<n and j<m:
		while i<n and a[i]==0:
			l.append(a[i])
			k+=1
			i+=1
		while j<m and b[j]==0:
			l.append(b[j])
			k+=1
			j+=1
		if i>=n or j>=m:
			break
		if a[i]!=0 and b[j]!=0 and a[i]>k and b[j]>k:
			f=1
			break
		if a[i]<=k:
			l.append(a[i])
			i+=1
		if b[j]<=k:
			l.append(b[j])
			j+=1
	if f==1:
		print(-1)
	else:
		while i<n:
			if a[i]!=0:
				if a[i]>k:
					f=1
					break
				else:
					l.append(a[i])
					i+=1
			else:
				l.append(a[i])
				k+=1
				i+=1
		while j<m:
			if b[j]!=0:
				if b[j]>k:
					f=1
					break
				else:
					l.append(b[j])
					j+=1
			else:
				l.append(b[j])
				k+=1
				j+=1
		if f==1:
			print(-1)
		else:
			print(*l)