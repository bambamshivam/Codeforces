for _ in range(int(input())):
	n=int(input())
	ar=list(map(int,input().split()))
	a=0
	while(max(ar)!=1):
		c=0
		for i in range(0,n):
			if(ar[i]!=1):
				break
			c+=1
		k=c
		while(k<n):
			t=ar[k]+k
			if(ar[k]!=1):
				ar[k]-=1
			k=t
		a+=1
	print(a)
