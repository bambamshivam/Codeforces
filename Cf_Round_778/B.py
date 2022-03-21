import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	s=S();d={}
	for i in s:d[i]=d.get(i,0)+1
	for i in range(len(s)):
		if d[s[i]]==1:print(s[i:]);break
		d[s[i]]-=1