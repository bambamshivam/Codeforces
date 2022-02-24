import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,x=M();a=L();d={};a.sort()
	for i in a:d[i]=d.get(i,0)+1
	for i in a:
		p=d.get(i,0);q=d.get(x*i,0)
		m=min(p,q)
		d[i]=d.get(i,0)-m
		d[x*i]=d.get(x*i,0)-m
	print(sum(list(d.values())))