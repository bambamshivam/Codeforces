for _ in range(int(input())):
	x,m,d=map(int,input().split())
	if(m*x>x+d):
		print(x+d)
	else:
		print(m*x)