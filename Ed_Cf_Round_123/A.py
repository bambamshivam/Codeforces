import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	s=S()
	a=s.find('r')
	b=s.find('R')
	c=s.find('g')
	d=s.find('G')
	e=s.find('b')
	f=s.find('B')
	if a<b and c<d and e<f:print("YES");continue
	print("NO")