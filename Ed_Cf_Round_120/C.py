import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M();a=sorted(L())
	s=sum(a);s1=0
	for i in range(1,n):s1+=a[i]-a[0]
	ans=max(math.ceil((s-s1-k)/n),0)+n-1
	for i in range(1,n):
		s1-=(a[i]-a[0])
		t=max(math.ceil((s-s1-k)/(n-i)),0)+n-i-1
		ans=min(ans,t)
	print(ans)