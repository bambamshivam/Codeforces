import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();l={};f=0;d={};l[sum(a)]=1
	for i in a:d[i]=d.get(i,0)+1
	while len(l)>0:
		l1={}
		for i in l:
			if d.get(i,0)==0 and i>1:
				l1[i//2]=l[i]+l1.get(i//2,0);l1[i-i//2]=l[i]+l1.get(i-i//2,0)
			elif d.get(i,0)>0:
				t=min(l[i],d[i])
				d[i]-=t
				if l[i]>t:
					if i==1:
						f=1;break
					else:
						l1[i//2]=l[i]-t+l1.get(i//2,0);l1[i-i//2]=l[i]-t+l1.get(i-i//2,0)
		if f:break
		l=l1
	for i in d:
		if d[i]>0:f=1;break
	print("NO" if f else "YES")