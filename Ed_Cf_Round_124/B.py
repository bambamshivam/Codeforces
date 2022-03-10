import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
t=1;l=[]
while t<=1000000000:l.append(t);t*=3
for _ in range(I()):
	n=I()
	if n<=len(l):print("YES");print(*l[:n]);continue
	print("NO")