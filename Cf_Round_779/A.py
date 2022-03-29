import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();s=S();l=[];ans=0
	for i in range(n):
		if s[i]=='0':l.append(i)
	for i in range(len(l)-1):ans+=max(2-l[i+1]+l[i]+1,0)
	print(ans)