import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m,k,q=M();l=[]
	for i in range(q):l.append(L())
	r=set();c=set();s=q
	for i in range(q-1,-1,-1):
		x,y=l[i];x-=1;y-=1
		if len(r)==n or len(c)==m or (x in r and y in c):s-=1
		r.add(x);c.add(y)
	print((pow(k,s,mod2)))