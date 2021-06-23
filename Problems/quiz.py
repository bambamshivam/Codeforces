for _ in range(int(input())):
	n,m,k=map(int,input().split())
	l=list(map(int,input().split()))
	ar=[0]*(n+m)
	a=[0]*n
	for i in range(k):
		ar[l[i]-1]+=1
	c=0
	for i in range(n):
		if(ar[i])>1:
			a[c]=i+1
			c+=1
	print(c,end=" ")
	for i in range(c):
		print(a[i],end=" ")

