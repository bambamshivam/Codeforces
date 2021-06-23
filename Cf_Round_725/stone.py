for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	a=l.index(min(l))
	b=l.index(max(l))
	ans=[0]*4
	ans[0]=max(a,b)+1
	ans[1]=max(n-a,n-b)
	ans[2]=a+1+n-b
	ans[3]=b+1+n-a
	print(min(ans))

