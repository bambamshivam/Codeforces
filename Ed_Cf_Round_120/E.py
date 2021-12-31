import io,os,sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
for _ in range(int(input())):
	n,m=map(int,input().split());x=list(map(int,input().split()));l=[]
	for i in range(n):l.append(input())
	c=1<<n;p=[0]*m;ans=-1
	for i in range(c):
		a=[0]*m;b=[0]*n;d=i
		for i in range(n):
			b[i]=d%2;d//=2
		for j in range(n):
			for k in range(m):
				if l[j][k]=='0':continue
				a[k]+=(1 if b[j]==1 else -1)
		s=0;p1=[0]*m
		ar=sorted(list(enumerate(a)),key=lambda x:x[1])
		for i in range(m):p1[ar[i][0]]=i+1
		for i in range(n):
			y=0
			for j in range(m):
				if l[i][j]=='0':continue
				y+=p1[j]
			s+=abs(x[i]-y)
		if s>ans:p=p1[:];ans=s
	print(*p)