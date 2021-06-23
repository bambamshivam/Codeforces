for _ in range(int(input())):
	n=int(input())
	s=input()
	di={}
	c=1
	for i in range(n):
		if s[i] in di:
			di[s[i]].append(i)
		else:
			di[s[i]]=[i]
	for ke in di:
		for j in range(len(di[ke])-1):
			if di[ke][j+1]-di[ke][j]!=1:
				print("NO")
				c=0
				break
		if c==0:
			break
	if c==1:
		print("YES")

