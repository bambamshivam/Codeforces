import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	s=S();n,m=M();l=[]
	for i in range(m):l.append(L()+[i])
	l.sort(key=lambda x:x[1]);s=0
	a=sorted(l[:2*n],key=lambda x:x[0])
	for i in range(2*n):s+=a[i][1]
	print(s)
	for i in range(n):print(a[i][2]+1,a[2*n-i-1][2]+1)