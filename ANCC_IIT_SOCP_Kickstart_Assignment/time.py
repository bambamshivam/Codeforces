for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	di={}
	for i in l:
		k=(i**4)%8
		if k in di:
			di[k]+=1
		else:
			di[k]=1
	for i in range(0,8):
		if i not in di:
			di[i]=0
	c=0
	for i in range(0,8):
		c+=((di[i]*(di[i]-1))//2)
	print(c)