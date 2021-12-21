import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	a,s=input().split()
	i=len(a)-1;j=len(s)-1;ans="";f=0
	while i>=0 and j>=0:
		if int(a[i])<=int(s[j]):
			ans+=str(int(s[j])-int(a[i]))
			i-=1;j-=1
		elif j==0 or s[j-1]!='1':f=1;break
		else:
			p=int(s[j-1]);q=int(s[j])
			ans+=str(10*p +q -int(a[i]))
			i-=1;j-=2
	if (j<0 and i>=0) or f==1:print(-1);continue
	ans=ans[::-1]
	if j>=0:
		ans=s[:j+1]+ans
	print(int(ans))