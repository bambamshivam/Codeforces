import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();s=S();i=c=0
	while i+1<n:
		if s[i]=='(':i+=2;c+=1
		else:
			j=i+1
			while j<n and s[j]!=')':j+=1
			if j<n:c+=1;i=j+1
			else:break
	print(c,n-i)