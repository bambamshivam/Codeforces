import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();b=L();m=math.inf;p=0
	if n==1:print(0);continue
	s=100*n+1;c=sum(a+b)
	dp=[[0 for i in range(s)] for j in range(n)]
	dp[0][a[0]]=1;dp[0][b[0]]=1
	for i in range(1,n):
		for j in range(1,s):
			if j>=a[i]:
				dp[i][j]=max(dp[i][j],dp[i-1][j-a[i]])
			if j>=b[i]:
				dp[i][j]=max(dp[i][j],dp[i-1][j-b[i]])
	for i in range(s):
		if dp[n-1][i]:
			if abs(c-2*i)<m:
				m=abs(c-2*i);p=i
	s1=sum((n-2)*i*i for i in a)+sum((n-2)*i*i for i in b)
	ans=p*p+(c-p)*(c-p)
	print(ans+s1)