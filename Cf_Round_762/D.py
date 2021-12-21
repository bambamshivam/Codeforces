import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	S()
	m,n=M();l=[];ans=0
	for i in range(m):l.append(L());ans=max(ans,sorted(l[-1])[-2])
	for i in range(n):
		a=0
		for j in range(m):
			a=max(a,l[j][i])
		ans=min(ans,a)
	print(ans)