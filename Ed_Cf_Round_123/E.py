import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();s=S()
	r=s.count('R');d=s.count('D')
	if r==0 or d==0:print(n);continue
	i=j=0;ans=n*n;f=1
	for k in range(len(s)):
		if k>0 and s[k]!=s[k-1]:f=0
		if f:ans-=n-1
		elif s[k]=='D':ans-=r-j
		else:ans-=d-i
		if s[k]=='D':i+=1
		else:j+=1
	print(ans)