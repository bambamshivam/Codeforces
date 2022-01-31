import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();ans=[];t=int(math.log2(n-1));a=2**t
	for i in range(n-1,a-1,-1):ans.append(i)
	ans.append(0)
	for i in range(1,a):ans.append(i)
	print(*ans)