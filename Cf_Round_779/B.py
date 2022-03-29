import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
l=[1]
for i in range(1,1002):
	l.append((l[-1]*i)%mod2)
for _ in range(I()):n=I();print((l[n//2]*l[n//2])%mod2 if n%2==0 else 0)