import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();b=[];c=[];f=0
	for i in a:
		if i%2==0:b.append(i)
		else:c.append(i)
	for i in range(len(b)-1):
		if b[i]>b[i+1]:f=1;break
	for i in range(len(c)-1):
		if c[i]>c[i+1]:f=1;break
	print("NO" if f else "YES")