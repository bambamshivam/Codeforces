import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l,r,k=M();ans=(r-l+1)//2
	if l==r:print("YES" if l!=1 else "NO");continue
	if l%2==1 and r%2==1:ans+=1
	print("YES" if ans<=k else "NO")