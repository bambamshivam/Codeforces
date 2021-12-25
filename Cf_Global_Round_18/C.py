import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=S();b=S()
	p=a.count('1');q=b.count('1');c=ans=0
	for i in range(n):c+=a[i]!=b[i]
	if p==q:
		if n-p+1==q:ans=min(c,n-c)
		else:ans=c
	elif n-p+1==q:ans=n-c
	else:ans=-1
	print(ans)