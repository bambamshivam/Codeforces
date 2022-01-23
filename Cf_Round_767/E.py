import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=[];ans=[[0]*n];res=0
	for i in range(n):l.append(L())
	for i in range(1,n):
		b=[]
		for j in range(n):
			a=l[i-1][j]
			if 0<=i-2<n:a^=ans[i-2][j]
			if 0<=j-1<n:a^=ans[i-1][j-1]
			if 0<=j+1<n:a^=ans[i-1][j+1]
			b.append(a)
		ans.append(b)
	for i in ans:
		for j in i:res^=j
	print(res)