import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M();e=n*k//2;o=n*k -e;p=1;q=2;res=[]
	if e%k!=0 or o%k!=0:print("NO");continue
	for i in range(o//k):
		l=[]
		for j in range(k):
			l.append(p);p+=2
		res.append(l)
	for i in range(e//k):
		l=[]
		for j in range(k):
			l.append(q);q+=2
		res.append(l)
	print("YES")
	for i in res:print(*i)