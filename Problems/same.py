for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	c=0
	di={}
	for i in range(n):
		if a[i]-i in di:
			di[a[i]-i]+=1
		else:
			di[a[i]-i]=1
	for ke in di:
		if di[ke]>1:
			c+=((di[ke]*(di[ke]-1))//2)
	print(c)