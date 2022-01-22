import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M();a=L();b=L();ans=k;s=set()
	for i in range(n):
		m=0;t=0
		for j in range(n):
			if j not in s and a[j]<=ans:
				if b[j]>m:
					t=j;m=b[j]
		s.add(t);ans+=m
	print(ans)