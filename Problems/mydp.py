for _ in range(int(input())):
	x,y,a,b=map(int,input().split())
	dp=[[0 for j in range(y+1)] for i in range(x+1)]
	for i in range(x+1):
		for j in range(y+1):
			a1=-1
			a2=-1
			if i-a>=0 and j-b>=0:
				a1=dp[i-a][j-b]
			if i-b>=0 and j-a>=0:
				a2=dp[i-b][j-a]
			dp[i][j]=max(a1,a2)+1

	print(dp[x][y])

