import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I()
	if n%2==0:print(n//2,n//2 -1,1)
	else:
		k=n-1
		if (k//2)%2==0:print(k//2 -1,k//2 +1,1)
		else:print(k//2 -2,k//2 +2,1)