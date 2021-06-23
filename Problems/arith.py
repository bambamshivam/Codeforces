for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if sum(l)>=n:
		print(sum(l)-n)
	else:
		print(1)