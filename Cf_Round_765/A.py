import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,l=M();a=L();s="";p=[0]*l
	for i in range(l):
		c=1<<i
		for j in a:
			p[i]+=(c&j==c)
	for i in range(l):
		if p[i]>n-p[i]:
			s+='1'
		else:
			s+='0'
	print(int(s[::-1],2))