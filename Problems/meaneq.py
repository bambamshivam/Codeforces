for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	b=0
	while(b==0):
		c=0
		for j in range(2*n):
			if(j==0):
				a1=l[2*n -1]
				n1=2*n -1
			else:
				a1=l[j-1]
				n1=j-1
			if(j==2*n-1):
				a2=l[0]
				n2=0
			else:
				a2=l[j+1]
				n2=j+1
			if((a1+a2)/2==l[j]):
				temp=l[n2]
				l[n2]=l[j]
				l[j]=temp
				c=1
		if(c==0):
			b=1
	for k in range(2*n):
		print(l[k],end=" ")

