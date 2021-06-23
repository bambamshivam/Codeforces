import math

for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	c=0
	a1=[]
	a2=[]

	for i in range(n):
		if l[i]%2==0:
			a1.append(l[i])
		else:
			a2.append(l[i])
	l=a1+a2
	l1=len(a1)
	a3=[]

	for i in a2:
		if i!=1:
			a3.append(i)

	a2=a3
	l2=len(a2)

	for i in range(l2):
		for j in range(i+1,l2):
			if math.gcd(a2[i],a2[j])>1:
				c+=1

	c+= ((n-1)*(n))//2 - ((n-l1-1)*(n-l1))//2
	print(c)

