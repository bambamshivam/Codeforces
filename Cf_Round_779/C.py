import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();c=L();f=1
	if c.count(1)!=1:print("NO");continue
	i=c.index(1);c=c[i:]+c[:i]
	for i in range(n-1):
		if c[i+1]>c[i]+1:f=0;break
	print("YES" if f else "NO")