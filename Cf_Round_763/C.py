import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	l=0;r=max(a);ans=min(a)
	while l<=r:
		m=(l+r)//2;f=1
		b=a[:];d=[0]*n
		for i in range(n-1,1,-1):
			t=min(b[i],max(0,b[i]+d[i]-m))//3
			b[i]-=3*t;d[i-1]+=t;d[i-2]+=2*t
		for i in range(n):
			if b[i]+d[i]<m:f=0;break
		if f==1:
			ans=max(m,ans);l=m+1
		else:
			r=m-1
	print(ans)