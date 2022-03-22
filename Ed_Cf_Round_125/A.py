import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	x,y=M()
	if x==y==0:print(0);continue
	if int((x*x+y*y)**0.5)**2==x*x+y*y:print(1);continue
	print(2)