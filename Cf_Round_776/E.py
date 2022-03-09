import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from heapq import heappop,heappush,heapify
for _ in range(I()):
	S();n,d=M();a=[0]+L();l=[];m=d;j=0
	for i in range(1,n+1):
		if a[i]-a[i-1]-1<m:m=a[i]-a[i-1]-1;j=i
	for i in range(n+1):
		if i!=j:l.append(a[i])
	def f(l):
		m1=max(l[i]-l[i-1]-1 for i in range(1,n))
		m2=min(l[i]-l[i-1]-1 for i in range(1,n))
		return min(m2,max(d-l[-1]-1,(m1-1)//2))
	ans=f(l)
	if j>1:l[j-1]=a[j]
	ans=max(ans,f(l));print(ans)