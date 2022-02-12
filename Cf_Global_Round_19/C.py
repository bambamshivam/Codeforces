import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	s=sum(a[1:n-1])
	o=sum(1 for i in range(1,n-1) if a[i]%2==1)
	e=sum(1 for i in range(1,n-1) if a[i]>1)
	if e==0 or (n==3 and o==1):print(-1);continue
	print(o + (s-o)//2)