def cpr(num):
	if num>1:
		for i in range(2,num//2 + 1):
			if num%i==0:
				return False
		return True
	else:
		return False


l=[]
m=2
for _ in range(int(input())):
	n=int(input())
	j=0
	if _!=0 and n<=m:
		t=0
		while t<len(l) and l[t]<=n:
			t+=1
		j=t-1
	else:
		for i in range(m,n+1):
			if cpr(i):
				l.append(i)
		j=len(l)-1
	c=j+1
	i=0
	
	while i<j:
		if l[i]*l[j]<=n:
			c-=(j-i)
			break
		else:
			j-=1
	m=n+1

	print(c)

