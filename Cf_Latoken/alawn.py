for _ in range(int(input())):
	n=int(input())
	l1=list(map(int,input().split()))
	l2=list(map(int,input().split()))
	l1i=[0]*n
	l2i=[0]*n
	v=[0]*n
	c=0
	for i in range(n):
		l1i[l1[i]-1]=i
	for i in range(n):
		l2i[l2[i]-1]=i
	for j in range(n):
		if v[j]==0:
			v[j]=1
			a1=l1[j]
			a2=l2[j]
			v[j]=1
			c+=1
			while a1!=-1 and a2!=-1:
				if a1!=-1:
					i2=l2i[a1-1]
					if v[i2]==0:
						v[i2]=1
						p=l1[i2]
					else:
						p=-1
				if a2!=-1:
					i1=l1i[a2-1]
					if v[i1]==0:
						v[i1]=1
						q=l2[i1]
					else:
						q=-1
				a1=p
				a2=q
	ans=1
	for i in range(c):
		ans=2 * ans % 1000000007
	print(ans)


