for _ in range(int(input())):
	a,b,c,d,k=map(int,input().split())
	if k-(abs(a-c)+abs(b-d))>=0 and (k-(abs(a-c)+abs(b-d)))%2==0:
		print("YES")
	else:
		print("NO")