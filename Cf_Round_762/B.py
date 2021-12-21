import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=1;ans=0;s=set()
	while a*a<=n:
		if a*a<=n and a*a not in s:ans+=1;s.add(a*a)
		if a*a*a<=n and a*a*a not in s:ans+=1;s.add(a*a*a)
		a+=1
	print(ans)