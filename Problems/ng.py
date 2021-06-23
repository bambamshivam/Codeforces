for _ in range(int(input())):
	a,b=map(int,input().split())
	if b==1:
		print("NO")
	else:
		print("YES")
		print(str(a)+" "+str(a*(2*b -1))+" "+str(a*b*2))