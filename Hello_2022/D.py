import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=[];ans=0
	for i in range(2*n):l.append(L())
	ans=sum(l[i][j] for i in range(n,2*n) for j in range(n,2*n))
	print(ans+min(l[0][n],l[0][2*n-1],l[n-1][n],l[n-1][2*n-1],l[n][0],l[n][n-1],l[2*n-1][0],l[2*n-1][n-1]))