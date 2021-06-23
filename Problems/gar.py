for t in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	print(n//2)
	for i in range(0,n-1,2):
		print(i+1, i+2, min(a[i],a[i+1]) , 10**9+7)