import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,x=M();a=L();p=[0]*(n+1);l=[0];ans=[]
	for i in range(n):p[i+1]=p[i]+a[i]
	for i in range(1,n+1):
		m=-math.inf
		for j in range(n-i+1):m=max(m,p[j+i]-p[j])
		l.append(m)
	for i in range(n+1):
		m=-math.inf
		for j in range(n+1):m=max(m,min(j,i)*x+l[j])
		ans.append(m)
	print(*ans)