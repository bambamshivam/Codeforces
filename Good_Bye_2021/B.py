import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();s=S();f=0
	for i in range(n-1):
		if s[i]<s[i+1]:f=1;break
	if f==1:
		print(min(s[0]+s[0],s[:i+1]+s[:i+1][::-1]))
	else:
		print(min(s[0]+s[0],s+s[::-1]))