for _ in range(int(input())):
	n=int(input())
	k=n
	c=1
	while k//10>0:
		k=k//10
		c+=1
	if n>=k*((10**c - 1)//9):
		print(9*(c-1) + k)
	else:
		print(9*(c-1) + k - 1)