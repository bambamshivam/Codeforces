import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	b=sorted(L())
	print(b[0],b[1],b[2] if b[2]!=b[0]+b[1] else b[3])