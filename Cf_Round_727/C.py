n,k,x=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
c=1
a=[]
for i in range(n-1):
	if l[i+1]-l[i]>x:
		f=(l[i+1]-l[i])
		d=0
		if f%x==0:
			d=f//x -1
		else:
			d=f//x
		a.append(d)
a.sort()
t=len(a)+1
i=0
s=0
while i<len(a) and k>=a[i]:
	k-=a[i]
	t-=1
	i+=1

print(t)
