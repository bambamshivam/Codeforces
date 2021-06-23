n,q=map(int,input().split())
ar=list(map(int,input().split()))
c=0
for i in range(0,n):
	if(ar[i]==1):
		c+=1
for i in range(0,q):
	t,x=map(int,input().split())
	if(t==1):
		if(ar[x-1]==1):
			ar[x-1]=0
			c-=1
		else:
			ar[x-1]=1
			c+=1
	else:
		if(x<=c):
			print(1)
		else:
			print(0)