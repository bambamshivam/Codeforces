import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l=sorted(S());t=S()
	a=l.count('a');b=l.count('b');c=l.count('c')
	if t!='abc' or a==0:print(a*'a'+b*'b'+c*'c'+''.join(l[a+b+c:]))
	else:print(a*'a'+c*'c'+b*'b'+''.join(l[a+b+c:]))