import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,c=M();a=L();d=[0]*(c+1);p=[0]*(c+1);f=1
	for i in a:d[i]=1
	for i in range(1,c+1):p[i]=p[i-1]+d[i]
	for i in a:
		if d[i]==1:
			d[i]=-1
			for j in range(i,c+1,i):
				if p[min(i+j-1,c)]-p[j-1] and d[j//i]==0:f=0;break
		if f==0:break
	print("YES" if f else "NO")