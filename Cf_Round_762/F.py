import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m,k=M()
	a=math.ceil(n/m);b=math.floor(n/m);c=(n%m)*a;cur=0
	for i in range(k):
		s=set()
		for j in range(n%m):
			l=[a]
			for t in range(a):
				l.append(cur%n +1);cur+=1;s.add(l[-1])
			print(*l)
		p=1
		for j in range(m- n%m):
			l=[b];t=0
			while t<b:
				if p not in s:
					l.append(p);t+=1
				p+=1
			print(*l)
	print()