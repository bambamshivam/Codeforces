import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m,r,c=M();l=[];ans=s=0
	for i in range(n):l.append(S());s+=l[-1].count('B')
	if s==0:ans=-1
	elif l[r-1][c-1]=='B':ans=0
	else:
		for i in range(n):
			if l[i][c-1]=='B':ans=1;break
		for i in range(m):
			if l[r-1][i]=='B':ans=1;break
		if ans!=1:ans=2
	print(ans)