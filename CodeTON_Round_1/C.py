import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=sorted(L());f=0
	for i in range(n-1):
		if a[i]+1==a[i+1]:f=1;break
	print("NO" if (f and 1 in a) else "YES")