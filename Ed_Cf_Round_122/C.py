import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	hc,dc=M();hm,dm=M();k,w,a=M();f=0
	for i in range(k+1):
		if ((hc+i*a)/dm) +1>hm/(dc + (k-i)*w) and ((hc+i*a)/dm) +1>math.ceil(hm/(dc + (k-i)*w)) and math.ceil(hm/(dc + (k-i)*w))>0:f=1;break
	print("YES" if f else "NO")