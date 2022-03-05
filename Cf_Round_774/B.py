import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=sorted(L());f=0;i=1;j=n-1;s1=a[0];s2=0
	while i<j:
		s1+=a[i];s2+=a[j];i+=1;j-=1
		if s1<s2:f=1;break
	print("YES" if f else "NO")