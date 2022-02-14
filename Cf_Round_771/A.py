import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	for i in range(n):
		if a[i]!=i+1:break
	j=a.index(i+1)
	b=a[:i]+a[i:j+1][::-1]+a[j+1:]
	print(*b)