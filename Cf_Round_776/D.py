import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=L();p=[0]*n;ans=[]
	for i in range(n,0,-1):
		l=l[:i]
		j=l.index(i)
		l=l[j+1:]+l[:j]
		ans.append((j+1-i)%(i))
	print(*ans[::-1])