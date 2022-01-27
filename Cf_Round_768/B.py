import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	j=n-2;ans=0
	while j>=0:
		while j>=0 and a[j]==a[-1]:
			j-=1
		if j<0:break
		k=n-1-j
		j-=k;ans+=1
	print(ans)