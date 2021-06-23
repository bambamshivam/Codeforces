for _ in range(int(input())):
	n,s,r=map(int,input().split())
	l=list(map(int,input().split()))
	c=0
	l=sorted(l)
	i=0
	h=n-1
	b=n-1
	while i<h:
		b=max(i,b)
		while b>i and l[i]+l[b]>=s:
			b-=1
		while h>b and l[i]+l[h]>r:
			h-=1
		c+=(h-b)
		i+=1
	print(c)
