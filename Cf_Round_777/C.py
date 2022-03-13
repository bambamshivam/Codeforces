import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n,m=M();l=[];ans=[]
	for i in range(n):l.append(S())
	if l[0][0]=='1':print(-1);continue
	for i in range(n):
		for j in range(m-1,0,-1):
			if l[i][j]=='1':ans.append([i+1,j,i+1,j+1])
	for i in range(n-1,0,-1):
		if l[i][0]=='1':ans.append([i,1,i+1,1])
	print(len(ans))
	for i in ans:print(*i)