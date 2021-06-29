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
	n=I()
	s=S()
	d=[0]*n
	k=[0]*n
	if s[0]=='D':
		d[0]=1
		k[0]=0
	else:
		d[0]=0
		k[0]=1
	for i in range(1,n):
		if s[i]=='D':
			d[i]=d[i-1]+1
			k[i]=k[i-1]
		else:
			k[i]=k[i-1]+1
			d[i]=d[i-1]
	t=[0]*n
	di={}
	for i in range(n):
		if d[i]==0 or k[i]==0:
			d1=k1=0
			if d[i]!=0:
				d1=1
			else:
				k1=1
			r=(d1,k1)
		else:
			g=math.gcd(d[i],k[i])
			r=(d[i]//g,k[i]//g)
		t[i]=r
		di[r]=0
	ar=[0]*n
	for i in range(n):
		di[t[i]]+=1
		ar[i]=di[t[i]]
	for i in range(n):
		print(ar[i],end=" ")
	print()



