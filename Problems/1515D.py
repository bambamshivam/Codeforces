import math
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

for _ in range(I()):
	n,l,r=M()
	a=L()
	cl=[0]*n
	cr=[0]*n
	c=0
	for i in range(l):
		cl[a[i]-1]+=1
	for i in range(l,n):
		if cl[a[i]-1]>0:
			cl[a[i]-1]-=1
			a[i]=-1
	for i in range(l,n):
		if a[i]!=-1:
			cr[a[i]-1]+=1
	s1=sum(cl)
	s2=sum(cr)
	t=min(s1,s2)
	ar=[]
	if t==s1:
		ar=cr
	else:
		ar=cl
	c+=t
	ar1=[]
	for i in range(len(ar)):
		if ar[i]>0:
			if ar[i]==1:
				ar1.append(ar[i])
			elif ar[i]%2==1:
				ar1.append(1)
				ar1.append(ar[i]-1)
			else:
				ar1.append(ar[i])
	ar1.sort()
	for i in range(len(ar1)):
		if ar1[i]>=t:
			ar1[i]-=t
			break
		else:
			t-=ar1[i]
			ar1[i]=0
	for i in range(len(ar1)):
		c+=ar1[i]//2
		ar1[i]%=2
	c+=sum(ar1)
	print(c)



