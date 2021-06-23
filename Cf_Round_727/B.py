n,q=map(int,input().split())
s=input()
d=[0]*n
c=0
for i in range(n):
	c+=ord(s[i])-96
	d[i]=c
for _ in range(q):
	a,b=map(int,input().split())
	if a-2<0:
		print(d[b-1])
	else:
		print(d[b-1]-d[a-2])