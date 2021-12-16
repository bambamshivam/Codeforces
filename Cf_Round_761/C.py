import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();l=[0]*(n+1);f=0;b=[0]*(n+1);s=set(a);c=0
	for i in range(n):
		if 1<=a[i]<=n and b[a[i]]==0:b[a[i]]+=1;continue
		l[min(n,a[i]- (a[i]//2) -1)]+=1
	for i in range(n-1,0,-1):
		if i+1 in s:l[i]+=(l[i+1])
		else:l[i]+=(l[i+1]-1)
	for i in range(1,n+1):
		if l[i]==0 and i not in s:f=1;break
	if f==1:print(-1);continue
	print(sum(1 for i in range(1,n+1) if i not in s))