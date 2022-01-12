import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	S();n,m=M();l=[L() for i in range(m)];ans=(1<<30)-1
	def find(u,p):
		if u==p[u]:return u
		p[u]=find(p[u],p)
		return p[u]
	def tree(edges):
		cnt=0;p=list(range(n+1))
		for i in edges:
			if cnt==n-1:break
			u,v,w=i;u=find(u,p);v=find(v,p)
			if u!=v:cnt+=1;p[u]=v
		return cnt==n-1
	for i in range(29,-1,-1):
		d=ans^(1<<i);cur=[j for j in l if j[2]|d==d]
		if tree(cur):ans=d
	print(ans)