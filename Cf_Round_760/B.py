import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I()
	a=list(input().split())
	s=a[0];f=0
	for i in range(1,n-2):
		if a[i][0]==s[-1]:s+=a[i][-1];continue
		else:s+=a[i];f=1
	if f==0:s+='a'
	print(s)