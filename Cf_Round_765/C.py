import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n,l,k=M();d=L()+[l];a=L()+[0]
dp=[[math.inf for j in range(k+1)] for i in range(n+1)]
dp[0][0]=l*a[0]
for i in range(1,n+1):
	for j in range(i):
		for t in range(k+1):
			if t+i-j-1>min(i,k):break
			dp[i][t+i-j-1]=min(dp[i][t+i-j-1],dp[j][t]+(l-d[i])*(a[i]-a[j]))
print(min(dp[-1]))