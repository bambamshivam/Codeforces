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
	if n%2==0:
		for i in range(0,n//2):
			k=2*(i+1)
			print(k,k-1,end=" ")
	else:
		for i in range((n-3)//2):
			k=2*(i+1)
			print(k,k-1,end=" ")
		print(n,n-2,n-1)
	print()
