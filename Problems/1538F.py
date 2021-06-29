def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

def co(n):
	k=p=n
	c=0
	while n>0:
		n//=10
		c+=1
	c-=1
	s=0
	t=0
	while c>0:
		x=k//(10**c)
		x-=t
		t+=x
		s+=((c+1)*x)
		p-=x
		c-=1
	s+=(p-1)
	return s


for _ in range(I()):
 	l,r=M()
 	print(co(r)-co(l))
