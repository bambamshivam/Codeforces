import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M();a=L();d={};f=0
	for i in a:d[i]=d.get(i,0)+1
	for i in d:
		if i+k in d:f=1;break
	print("YES" if f else "NO")