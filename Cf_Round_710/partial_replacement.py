def SI():
	return input()
def MI():
	return map(int,input().split())
def II():
	return int(input())
def LI():
	return list(map(int,input().split()))
for _ in range(int(input())):
	n,k=MI()
	s=SI()
	l=list(s)
	if l.count('*')==1:
		print(1)
	else:
		i1=l.index('*')
		i2=n-1-l[::-1].index('*')
		c=2
		i=i1
		while i<i2:
			if i+k<i2:
				c+=1
				i3=i+k-l[i:i+k+1][::-1].index('*')
				i=i3
			else:
				break
		print(c)



