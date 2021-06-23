for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	c=l[0]+l[n-1]
	for i in range(0,n-1):
		c+=abs(l[i]-l[i+1])
	for i in range(1,n-1):
		if l[i]>l[i-1] and l[i]>l[i+1]:
			c-=(l[i]-max(l[i+1],l[i-1]))
			l[i]=max(l[i+1],l[i-1])
			
	if n>=2 and l[0]>l[1]:
		c-=(l[0]-l[1])
		l[0]=l[1]
	if n>=2 and l[n-1]>l[n-2]:
		c-=(l[n-1]-l[n-2])
		l[n-1]=l[n-2]
	if n==1:
		c-=l[0]
	print(c)


