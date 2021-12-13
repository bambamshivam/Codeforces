import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n=I();a=L();inv=0;v=[0]*n
	if n!=len(set(a)):print("YES");continue
	for i in range(n):
		if v[i] or a[i]==i+1:continue
		cur=a[i]
		while cur!=i+1:
			v[cur-1]=1
			inv+=1
			cur=a[cur-1]
	print("NO" if inv%2 else "YES")