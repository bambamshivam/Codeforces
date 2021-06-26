for _ in range(int(input())):
	n,x,m=map(int,input().split())
	l=u=x
	for i in range(m):
		a,b=map(int,input().split())
		if a<=l<=b or a<=u<=b:
			l=min(l,a)
			u=max(u,b)
	print(u-l+1)