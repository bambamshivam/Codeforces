import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M()
	if n==4 and k==n-1:print(-1);continue
	if k!=n-1:
		l=[0,n-1,k,n-k-1]
		for i in range(n//2):
			if i not in l:print(i,n-i-1)
		print(k,n-1)
		if k!=0:print(0,n-k-1)
	else:
		print(1,3);print(n-1,n-2)
		print(0,n-4);print(2,n-3)
		for i in range(4,n//2):
			print(i,n-i-1)