import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m,a,b,c,d=M();ans=math.inf
	if c>=a:
		ans=min(ans,c-a)
	else:
		ans=min(ans,n-a+n-c)
	if d>=b:
		ans=min(ans,d-b)
	else:
		ans=min(ans,m-b+m-d)
	print(ans)