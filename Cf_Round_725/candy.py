for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if sum(l)%(len(l))!=0:
		print(-1)
	elif max(l)==min(l):
		print(0)
	else:
		c=0
		avg=sum(l)//len(l)
		for i in l:
			if i>avg:
				c+=1
		print(c)

