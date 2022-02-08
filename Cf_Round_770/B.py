import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,x,y=M();a=L();s=sum(a)
	if (x+s)%2==y%2:print("Alice");continue
	print("Bob")