import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L()
	if len(a)>1 and (max(a)-1 not in a and a.count(max(a))==1):print("NO");continue
	if len(a)==1 and a[0]>1:print("NO");continue
	print("YES")