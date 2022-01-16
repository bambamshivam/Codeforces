import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();adj=[[] for i in range(n)];d=[0]*n;e={};ans=[0]*(n-1);ok=1
	for i in range(n-1):
		a,b=M();a-=1;b-=1
		adj[a].append(b)
		adj[b].append(a)
		d[a]+=1;d[b]+=1
		if a>b:a,b=b,a
		e[(a,b)]=i
	for i in range(n):
		if d[i]>2:ok=0
	if not ok:print(-1);continue
	j=d.index(1);c=2;q=[j];v=[0]*n;v[j]=1
	while q:
		r=q.pop()
		for j in adj[r]:
			if v[j]==1:continue
			a=j;b=r;v[j]=1
			if a>b:a,b=b,a
			ans[e[(a,b)]]=c
			q.append(j)
		c=2 if c==3 else 3
	print(*ans)