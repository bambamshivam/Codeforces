import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l,r,a=M()
	t=r//a
	if t*a-1<l:print(t + r%a)
	else:print(max(t+r%a,t-1 + (t*a-1)%a))