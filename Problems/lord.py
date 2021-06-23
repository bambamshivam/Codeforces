for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	print(6*(n//2))
	for k in range(n//2):
		i=2*k
		print(str(1)+" "+str(i+1)+" "+str(i+2))
		print(str(2)+" "+str(i+1)+" "+str(i+2))
		print(str(1)+" "+str(i+1)+" "+str(i+2))
		print(str(2)+" "+str(i+1)+" "+str(i+2))
		print(str(1)+" "+str(i+1)+" "+str(i+2))
		print(str(2)+" "+str(i+1)+" "+str(i+2))
