for _ in range(int(input())):
	n=int(input())
	if n==2:
		print(-1)
	else:
		di={}
		a1=1
		if n%2==0:
			a2=(n**2 // 2)+1
		else:
			a2=(n**2 // 2)+2
		a=[[0 for i in range(n)] for j in range(n)]
		for i in range(n):
			for j in range(n):
				if (i+j)%2==0:
					a[i][j]=a1
					a1+=1
				else:
					a[i][j]=a2
					a2+=1
		for i in range(n):
			for j in range(n):
				print(a[i][j],end=" ")
			print()