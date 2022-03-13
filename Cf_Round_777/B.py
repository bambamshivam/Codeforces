import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m=M();l=[];f=0
	for i in range(n):l.append(S())
	for i in range(n-1):
		for j in range(m-1):
			if int(l[i][j])+int(l[i][j+1])+int(l[i+1][j])+int(l[i+1][j+1])==3:f=1;break
	print("NO" if f else "YES")