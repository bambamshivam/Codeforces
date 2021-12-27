import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();p=L();s=S()
	a=[];b=[];ans=[0]*n
	for i in range(n):
		if s[i]=='1':
			a.append((p[i],i))
		else:
			b.append((p[i],i))
	a.sort(key=lambda x:x[0])
	b.sort(key=lambda x:x[0])
	k=len(a);j=len(b);t=0
	for i in range(n-k+1,n+1):
		ans[a[t][1]]=i;t+=1
	for i in range(j):
		ans[b[i][1]]=i+1
	print(*ans)