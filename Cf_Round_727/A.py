for _ in range(int(input())):
	n,x,t=map(int,input().split())
	k=t//x
	if n<=k:
		print((n*n- n)//2)
	else:
		print((n-k-1)*k + (k*(k+1))//2)


