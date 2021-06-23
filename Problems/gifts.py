for _ in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	l.sort(reverse=True)
	sum1=0
	sum2=0
	for i in range(2*k):
		if i%2==0:
			sum1+=l[i]
		else:
			sum2+=l[i]
	if(sum2+l[2*k]>sum1):
		print(sum2+l[2*k])
	else:
		print(sum1)