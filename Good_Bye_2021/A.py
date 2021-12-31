import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();d={};ans=0
	for i in a:d[abs(i)]=d.get(abs(i),0)+1
	for i in d:ans+=1+(d[i]>1 and i!=0)
	print(ans)