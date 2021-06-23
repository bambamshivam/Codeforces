import math
def fact(n):
	if n==1:
		return 0
	c=1
	i=2
	while i<=math.sqrt(n):
		if n%i==0:
			n//=i
			c+=1
			i-=1
		i+=1
	return c

for _ in range(int(input())):
	a,b,k=map(int,input().split())
	if fact(a)+fact(b)>=k and (k>=2 or (max(a,b)%min(a,b)==0 and a!=b)):
		print("YES")
	else:
		print("NO")