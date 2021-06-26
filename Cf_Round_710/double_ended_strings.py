def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(MI())
for _ in range(I()):
	s1=S()
	s2=S()
	n=len(s1)
	m=len(s2)
	dp=[[0 for i in range(m+1)] for j in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,m+1):
			if s1[i-1]==s2[j-1]:
				dp[i][j]=1+dp[i-1][j-1]
			else:
				dp[i][j]=0
	t=-1
	for i in dp:
		t=max(t,max(i))
	print(n+m-2*t)
