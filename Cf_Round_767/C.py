import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();b=[];d={};cur=0
	for i in range(n):d[a[i]]=d.get(a[i],0)+1
	for i in range(n+1):
		if d.get(i,0)==0:cur=i;break
	i=0
	while i<n:
		if cur==0:i+=1;b.append(cur);continue
		j=i;m=cur;s=set()
		while j<n:
			if len(s)==cur:break
			d[a[j]]-=1
			if d[a[j]]==0:m=min(m,a[j])
			if a[j]<cur and a[j] not in s:s.add(a[j])
			j+=1
		b.append(cur);i=j;cur=m
	print(len(b));print(*b)