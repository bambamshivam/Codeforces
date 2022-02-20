import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	if a==sorted(a):print(0);continue
	if a[-1]<a[-2]:print(-1);continue
	i=n-3;m=min(a[-1],a[-2])
	while i>=0 and a[i]<=a[i+1]:m=min(a[i],m);i-=1
	if a[i+1]-a[-1]>a[i+1]:print(-1);continue
	print(i+1)
	for j in range(i+1):print(j+1,i+2,n)