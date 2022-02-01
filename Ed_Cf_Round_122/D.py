import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import deque
for _ in range(I()):
	n,k=M();b=L();c1=L();l=[]
	q=deque([[1,0]]);d=[math.inf]*1001;d[1]=0
	while q:
		i,c=q.popleft()
		for j in range(1,i+1):
			if i+i//j>1000:continue
			if d[i+i//j]>c+1:
				d[i+i//j]=c+1
				q.append([i+i//j,c+1])
	for i in range(n):l.append(d[b[i]])
	if k<sum(l):
		wt=l;val=c1;w=k;s=0
		dp=[[0 for i in range(w+1)] for j in range(n+1)]
		for i in range(1,n+1):
			if wt[i-1]==0:s+=val[i-1]
			dp[i][0]=s
		for i in range(1,n+1):
			for j in range(1,w+1):
				if wt[i-1]>j:
					dp[i][j]=dp[i-1][j]
				else:
					dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
		print(dp[n][w])
	else:print(sum(c1))