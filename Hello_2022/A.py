import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,k=M()
	if n%2==0:
		if k>n//2:
			print(-1)
		else:
			l=[['.' for i in range(n)] for j in range(n)]
			for i in range(0,2*k,2):
				l[i][i]='R'
			for i in l:
				print(''.join(i))
	else:
		if k>n//2 +1:
			print(-1)
		else:
			l=[['.' for i in range(n)] for j in range(n)]
			for i in range(0,2*k,2):
				l[i][i]='R'
			for i in l:
				print(''.join(i))
		