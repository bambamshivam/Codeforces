import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();ans=0;m=math.inf
	for i in range(10**(len(str(n))-1),10**len(str(n))):
		if i%7!=0:continue
		s1=str(i);c=0
		for i in range(len(s1)):
			if s1[i]!=str(n)[i]:c+=1
		if c<m:ans=int(s1);m=c
	print(ans)