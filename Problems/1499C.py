import math;import heapq
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())


#start here
for _ in range(I()):
	n=I()
	l=L()
	m1=l[0]
	m2=l[1]
	a=[(m1,m2),(m1,m2)]
	for i in range(2,n):
		if i%2==0:
			if l[i]<m1:
				m1=l[i]
		else:
			if l[i]<m2:
				m2=l[i]
		a.append((m1,m2))
	p=n*(l[0]+l[1])
	k=0
	ar=[]
	for i in range(n):
		k+=l[i]
		ar.append(k)
	for i in range(2,n):
		(m1,m2)=a[i]
		e=(i//2) + 1
		o=(i+1)-e
		s=(ar[i]-m1-m2) + (n-e+1)*m1 + (n-o+1)*m2
		if s<p:
			p=s
	print(p)