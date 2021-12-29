import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m,a,b,c,d,p=M()
	p=(1 - p*pow(100,mod1-2,mod1))%mod1;dr=-1;dc=-1;u=0;v=1
	for i in range(4*(n-1)*(m-1)):
		if not (1<=a+dr<=n):dr*=-1
		if not (1<=b+dc<=m):dc*=-1
		a+=dr;b+=dc;u+=1
		if a==c or b==d:
			u=(u*p)%mod1;v=(v*p)%mod1
	print((u*pow(1-v,mod1-2,mod1))%mod1)