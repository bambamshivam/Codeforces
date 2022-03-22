import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,b,x,y=M();ans=s=0
	for i in range(n):
		if s+x<=b:
			s+=x;ans+=s
		else:
			s-=y;ans+=s
	print(ans)