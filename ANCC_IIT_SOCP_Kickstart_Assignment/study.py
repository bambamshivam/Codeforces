n,k=map(int,input().split())
l=list(map(int,input().split()))
c=i=0
t=sum(l)
if t==0:
	print(0)
else:
	d=[0]*((t//k)-1)
	while l[i]==0:
		i+=1
	while i<n:
		c+=l[i]
		if c==t:
			break
		if c%k==0:
			d[(c//k) - 1]+=1
		i+=1
	s=1
	for i in d:
		s=(s*i)%((10**9) + 7)
	print(s%((10**9) + 7))