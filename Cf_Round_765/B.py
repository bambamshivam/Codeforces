import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
for _ in range(I()):
	n=I();a=L();d=defaultdict(list)
	for i in range(n):d[a[i]].append(i)
	def f(m):
		for ke in d:
			if len(d[ke])>1:
				for j in range(len(d[ke])-1):
					if n-d[ke][j+1]+d[ke][j]>=m:
						return True
		return False
	l=1;r=n-1;ans=-1
	while l<=r:
		m=(l+r)//2
		if f(m):
			ans=m;l=m+1
		else:
			r=m-1
	print(ans)