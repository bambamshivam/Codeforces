import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	s=S();f=0;l=list(s)
	for i in range(len(s)-1,0,-1):
		if int(s[i-1])+int(s[i])>=10:
			s1=str(int(s[i-1])+int(s[i]))
			l[i-1]=s1[0];l[i]=s1[1]
			print(''.join(l));f=1;break
	if f==0:
		ans=str(int(s[0])+int(s[1]))
		for i in range(2,len(s)):ans+=s[i]
		print(ans)