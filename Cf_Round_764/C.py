import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
for _ in range(I()):
	n=I();a=L();d=defaultdict(set)
	for i in range(n):
		p=a[i]
		while p>0:
			d[i].add(p);p//=2
	p=[[] for i in range(n)]
	for i in range(n):
		for ke in d:
			if i+1 in d[ke]:
				p[i].append(ke)
	p.sort(key=lambda x:len(x))
	v=[0]*n;ok=1
	for i in range(n):
		f=0
		for j in range(len(p[i])):
			if v[p[i][j]]==0:v[p[i][j]]=1;f=1;break
		if f==0:ok=0;break
	print("YES" if ok else "NO")