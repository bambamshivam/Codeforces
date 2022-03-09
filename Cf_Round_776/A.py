import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	s=S();c=S();f=0
	for i in range(len(s)):
		if s[i]==c and i%2==0:f=1;break
	if f==0:print("NO");continue
	print("YES")