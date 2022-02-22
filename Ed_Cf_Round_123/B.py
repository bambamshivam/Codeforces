import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I()
	l=list(range(n,0,-1))
	print(*l)
	for i in range(n-1):
		l[i],l[i+1]=l[i+1],l[i]
		print(*l)
		l[i],l[i+1]=l[i+1],l[i]