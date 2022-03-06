import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import defaultdict
n,m=M();l=[];d=defaultdict(list);ans=0
for i in range(n):l.append(L())
for i in range(n):
	for j in range(m):
		d[l[i][j]].append([i,j])
for ke in d:
	x=[];y=[]
	for i in d[ke]:x.append(i[0]);y.append(i[1])
	x.sort();y.sort();s1=sum(x);s2=sum(y);p=len(x)
	for i in range(p):
		s1-=x[i];ans+=abs((p-i-1)*x[i]-s1)
		s2-=y[i];ans+=abs((p-i-1)*y[i]-s2)
print(ans)