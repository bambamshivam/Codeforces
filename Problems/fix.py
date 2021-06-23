def chbi(adj,c):
	c[0]=1
	q=[0]
	while q:
		i=q.pop()
		for j in range(len(adj[i])):
			n=adj[i][j]
			if c[n]==-1:
				c[n]=1-c[i]
				q.append(n)
			else:
				if c[n]==c[i]:
					return False
	return True

for _ in range(int(input())):
	n,m=map(int,input().split())
	v=list(map(int,input().split()))
	t=list(map(int,input().split()))
	c=[-1]*n
	adj=[[] for i in range(n)]
	for i in range(m):
		a,b=map(int,input().split())
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
	if (sum(v)-sum(t))%2!=0:
		print("NO")
	elif chbi(adj,c):
		s1=s2=0
		for i in range(n):
			if c[i]==0:
				s1+=(t[i]-v[i])
			else:
				s2+=(t[i]-v[i])
		if s1!=s2:
			print("NO")
		else:
			print("YES")
	else:
		print("YES")