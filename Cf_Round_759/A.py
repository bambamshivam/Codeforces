import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n=I()
	a=L()
	ans=1+a[0]
	for i in range(1,n):
		if a[i]==1:
			if a[i-1]==1:
				ans+=5
			else:
				ans+=1
		else:
			if a[i-1]==0:
				ans=-1;break
	print(ans)