import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n=I()
	a=L();m=max(a)
	if a[-1]==m:print(0);continue
	ans=1;cur=a[-1]
	for i in range(n-2,-1,-1):
		if a[i]==m:
			break
		if a[i]>cur:
			ans+=1
			cur=a[i]
	print(ans)