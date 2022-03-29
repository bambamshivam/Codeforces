import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l,r=M();a=L();ans=''
	for i in range(18):
		c=0
		for j in a:
			if j&(1<<i):c+=1
		if c>r-l+1-c:ans+='1'
		else:ans+='0'
	print(int(ans[::-1],2))