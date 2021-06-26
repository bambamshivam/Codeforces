def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

for _ in range(I()):
	n=I()
	l=L()
	c=0
	for i in range(n):
		for j in range(l[i]-i-2,n,l[i]):
			if l[i]*l[j]==i+j+2:
				c+=1
	print(c)

