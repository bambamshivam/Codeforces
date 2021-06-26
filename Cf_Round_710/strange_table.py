for _ in range(int(input())):
	n,m,x=map(int,input().split())
	c=x//n + 1
	r=x%n
	if r==0:
		r=n
		c-=1
	print((r-1)*m + c)