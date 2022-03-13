import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();t=n//3;s='21'*t
	if n%3==1:print('1'+s)
	elif n%3==2:print(s+'2')
	else:print(s)