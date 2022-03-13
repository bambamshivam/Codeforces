import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	x,d=M();c=0
	def p(x):
		for i in range(2,int(x**0.5) +1):
			if x%i==0:return i
		return -1
	while x%d==0:x//=d;c+=1
	if c==1:print("NO");continue
	if p(x)!=-1:print("YES");continue
	if p(d)!=-1 and d==p(d)*p(d) and x==p(d) and c==3:print("NO");continue
	if c>2 and p(d)!=-1:print("YES");continue
	print("NO")