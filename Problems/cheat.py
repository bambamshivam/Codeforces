for _ in range(int(input())):
	n,k,f=map(int,input().split())
	ar=[0]*n
	for i in range(n):
		s,e=map(int,input().split())
		ar[i]=(s,e)
	a=sorted(ar,key=lambda x:x[0])
	l=[]
	l.append(a[0])
	for i in range(n):
		(c,b)=l[-1]
		if a[i][0]<=b and a[i][-1]<=b:
			continue
		elif a[i][0]<=b and a[i][-1]>b:
			l.pop()
			l.append((c,a[i][-1]))
		else:
			l.append(a[i])
	c=0
	for i in range(len(l)):
		c+=(l[i][-1]-l[i][0])
	if f-c>=k:
		print("YES")
	else:
		print("NO")





