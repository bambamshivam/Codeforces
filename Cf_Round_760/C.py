import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I()
	a=L()
	g1=g2=f1=f2=0
	for i in range(0,n,2):
		g1=math.gcd(g1,a[i])
	for i in range(1,n,2):
		g2=math.gcd(g2,a[i])
	for i in range(0,n,2):
		if a[i]%g2==0:f1=1;break
	for i in range(1,n,2):
		if a[i]%g1==0:f2=1;break
	if f1==0:
		print(g2)
	elif f2==0:
		print(g1)
	else:
		print(0)