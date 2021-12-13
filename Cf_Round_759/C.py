import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n,k=M()
	a=L()
	b=[i for i in a if i!=0];ans=0
	b.append(0);b.sort()
	p=b.index(0)
	i=min(p,k);j=max(len(b)-1-k,p);i1=i;j1=j
	ans+=abs(b[i])+b[j]
	while i!=p:
		ans+=b[min(p,i+k)]-b[i]+2*abs(b[min(p,i+k)])
		i=min(p,i+k)
	while j!=p:
		ans+=b[j]-b[max(p,j-k)]+2*b[max(p,j-k)]
		j=max(p,j-k)
	a1=b[j1]+2*b[-1]-b[j1]-b[0]
	a2=abs(b[i1])+b[i1]-2*b[0]+b[-1]
	ans+=min(a1,a2)
	print(ans)