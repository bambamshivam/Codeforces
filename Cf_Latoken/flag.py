for _ in range(int(input())):
	n,m=map(int,input().split())
	l=[" " for i in range(n)]
	a=[" " for i in range(n)]
	b=[" " for i in range(n)]
	for i in range(n):
		l[i]=input()
		if i%2==0:
			a[i]="RW"*(m//2)
			a[i]+="R"*(m - 2*(m//2))
			b[i]="WR"*(m//2)
			b[i]+="W"*(m - 2*(m//2))
		else:
			b[i]="RW"*(m//2)
			b[i]+="R"*(m - 2*(m//2))
			a[i]="WR"*(m//2)
			a[i]+="W"*(m - 2*(m//2))
	c1=1
	c2=1
	for i in range(n):
		for j in range(m):
			if l[i][j]!=".":
				if l[i][j]!=a[i][j]:
					c1=0
					break
		if c1==0:
			break
	for i in range(n):
		for j in range(m):
			if l[i][j]!=".":
				if l[i][j]!=b[i][j]:
					c2=0
					break
		if c2==0:
			break
	if c1+c2>0:
		print("YES")
	else:
		print("NO")
	if c1!=0:
		for i in range(n):
			print(a[i])
	elif c2!=0:
		for i in range(n):
			print(b[i])


