import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I();a=L();m=max(a);s=set(a);ans=0
for i in range(1,m+1):
	if i in s:continue
	g1=0
	for j in range(2*i,m+1,i):
		if j in s:
			g1=math.gcd(g1,j)
			if g1==i:s.add(i);ans+=1;break
print(ans)