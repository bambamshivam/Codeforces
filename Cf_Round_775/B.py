import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();ans=1;s=sum(a)
	if max(a)==0:print(0);continue
	for i in range(n):ans=max(ans,2*a[i]-s)
	print(ans)