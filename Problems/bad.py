for _ in range(int(input())):
	n,m,i,j=map(int,input().split())
	a=[0]*4
	a[0]=(i-1)+(j-1)
	a[1]=(n-i)+(j-1)
	a[2]=(i-1)+(m-j)
	a[3]=(n-i)+(m-j)
	if max(a)==a[0] or max(a)==a[3]:
		print(1,1,n,m)
	else:
		print(n,1,1,m)