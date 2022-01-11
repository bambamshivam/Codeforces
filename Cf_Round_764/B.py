import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	a,b,c=M();f=0
	if 2*b-c>0 and (b-c+b)%a==0:f=1
	if (c-a)%2==0 and a+(c-a)//2>0 and (a+ (c-a)//2)%b==0:f=1
	if 2*b-a>0 and (b+(b-a))%c==0:f=1
	print("YES" if f else "NO")