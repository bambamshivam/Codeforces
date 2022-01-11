import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M();s=S();ans=0;d={};c=0
	for i in s:d[i]=d.get(i,0)+1
	for ke in d:c+=d[ke]//2
	l=1;r=n
	while l<=r:
		m=(l+r)//2
		if m*k<=n and c>=(m//2)*k:
			ans=m;l=m+1
		else:
			r=m-1
	print(ans)