import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l,r=M();ans=1000000
	for i in range(18):
		t=1<<i
		p=l//t
		if p%2==0:
			q=l%t + (p//2)*t
		else:
			q=(p//2 +1)*t
		a=(r+1)//t
		if a%2==0:
			b=(r+1)%t + (a//2)*t
		else:
			b=(a//2 +1)*t
		ans=min(ans,b-q)
	print(ans)