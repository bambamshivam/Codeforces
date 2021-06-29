import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(input())
def L():
	return list(map(int,input().split()))

for _ in range(I()):
	n=I()
	u=L()
	s=L()
	l=[[] for i in range(n)]
	for i in range(n):
		l[u[i]-1].append(s[i])
	
	ar=[]
	t=-1
	for i in l:
		if len(i)>t:
			t=len(i)
		if len(i)!=0:
			ar.append(i)
	for i in ar:
		i.sort(reverse=True)

	a=[]

	for i in range(len(ar)):
		s=0
		a.append([])
		for j in range(len(ar[i])):
			s+=ar[i][j]
			a[-1].append(s)
	ss=[0]*n


	for i in range(len(a)):
		for j in range(len(a[i])):
			k=len(a[i]) - (len(a[i])%(j+1))
			ss[j]+=a[i][k-1]

	for i in range(n):
		print(ss[i],end=" ")
	print()

