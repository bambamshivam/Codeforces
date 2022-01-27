import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();b=L();l=[]
	m=max(max(a),max(b))
	for i in range(n):
		l.append(min(a[i],b[i]))
	print(m*max(l))