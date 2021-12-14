import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();b=L()
	s=sum(b);f=0;ans=[0]*n
	if s%(n*(n+1)//2)!=0:print("NO");continue
	s//=(n*(n+1)//2)
	for i in range(n):
		cur=s-b[(i+1)%n]+b[i]
		if cur>0 and cur%n==0:
			ans[(i+1)%n]=cur//n
		else:f=1;break
	if f:print("NO");continue
	print("YES");print(*ans)