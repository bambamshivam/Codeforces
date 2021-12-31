import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();ans=math.inf;e=pow(10,-7)
	if n==1:print(0);continue
	for i in range(n):
		for j in range(i+1,n):
			d=(a[j]-a[i])/(j-i)
			s1=a[i]-i*d;s2=a[i]+i*d;cur1=cur2=0
			for k in range(n):
				cur1+=(abs(a[k]-s1)>e);s1+=d
				cur2+=(abs(a[k]-s2)>e);s2-=d
			ans=min(ans,cur1,cur2)
	print(ans)