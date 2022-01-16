import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m=M();d=[(1,1),(n,1),(1,m),(n,m)];a=[]
	for i in range(1,n+1):
		for j in range(1,m+1):
			mi=math.inf;ma=0
			for k in range(4):
				mi=min(mi,abs(i-d[k][0])+abs(j-d[k][1]))
				ma=max(ma,abs(i-d[k][0])+abs(j-d[k][1]))
			a.append((mi,ma))
	a.sort();ans=[]
	for i in a:ans.append(i[1])
	print(*ans[::-1])