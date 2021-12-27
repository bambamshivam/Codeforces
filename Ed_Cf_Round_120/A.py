import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	l=sorted(L())
	if len(set(l))==3:
		print("YES" if l[0]+l[1]==l[2] else "NO")
	else:
		if (l[0]==l[1] and l[2]%2==0) or (l[1]==l[2] and l[0]%2==0):
			print("YES")
		else:
			print("NO")