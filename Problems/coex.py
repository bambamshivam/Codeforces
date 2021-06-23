for _ in range(int(input())):
	n=int(input())
	l=[]
	for i in range(n):
		l+=[int(input())]
	a=[[l[0]]]
	for i in range(1,n):
		if l[i]==1:
			a+=[a[-1]+[1]]
		else:
			j=len(a[-1])-1
			while a[-1][j]+1!=l[i]:
				j-=1
			a+=[a[-1][:j]+[l[i]]]
	for i in range(len(a)):
		for j in range(len(a[i])-1):
			print(str(a[i][j])+".",end="")
		print(a[i][-1])
