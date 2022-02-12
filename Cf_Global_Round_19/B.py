import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();ans=0
	for i in range(n):
		for j in range(i,n):
			b=a[i:j+1]
			for k in b:
				if k==0:ans+=2
				else:ans+=1
	print(ans)