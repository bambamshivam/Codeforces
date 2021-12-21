import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import Counter
for _ in range(I()):
	n=I();a=sorted(L());s=set();cost=0;ans=[];c=Counter(a);j=0;l=[];f=0
	for i in range(n+1):
		ans.append(cost+c[i])
		while j<n and a[j]==i:
			if a[j] not in s:s.add(a[j])
			else:l.append(a[j])
			j+=1
		if i==n:break
		if i not in s:
			if not l:f=1;break
			cost+=i-l.pop()
	if f==1:ans=ans+[-1]*(n+1-len(ans))
	print(*ans)