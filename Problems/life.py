for _ in range(int(input())):
	n,m=map(int,input().split())
	str=input()
	l=[]
	a=[]
	for i in range(len(str)):
		if str[i]=='1':
			l.append(i)
	if len(l)==0:
		print(str)
	else:
		g=min(l[0],m)
		a.append((l[0]-g,max(0,l[0]-1)))
		for i in range(len(l)-1):
			q=l[i+1]-1-l[i]
			if q>=2*m:
				a.append((l[i]+1,l[i]+m))
				a.append((l[i+1]-m,l[i+1]-1))
			elif q>1 and q<2*m:
				if q%2==0:
					a.append((l[i]+1,l[i+1]-1))
				else:
					a.append((l[i]+1,l[i]+ q//2))
					a.append((l[i+1]- q//2,l[i+1]-1))
		g=min(n-1-l[-1],m)
		a.append((min(l[-1]+1,n-1),l[-1]+g))
		for i in range(len(a)):
			r=a[i][0]
			t=a[i][-1]
			str=str[:r]+'1'*(t-r+1)+str[t+1:n]
		print(str)

