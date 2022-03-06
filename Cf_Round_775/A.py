import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	if 0 not in a:print(0);continue
	i=a.index(0);j=n-a[::-1].index(0)-1
	print(j-i+2)