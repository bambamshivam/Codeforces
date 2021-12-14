import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M()
	a=sorted(L())
	ans=sum(a[:n-2*k])
	i=n-2*k;j=n-k
	while j<n:
		ans+=(a[i]//a[j])
		i+=1;j+=1
	print(ans)