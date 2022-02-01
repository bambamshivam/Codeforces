import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	s=S();n=len(s);a=s.count('1');b=n-a
	if n<=2:print(0);continue
	if a==b:print(a-1);continue
	print(b if a>b else a)