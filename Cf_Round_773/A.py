import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	x1,y1=M();x2,y2=M();x3,y3=M()
	y=[y1,y2,y3]
	if len(set(y))==2 and y.count(min(y))==1:
		m=max(y);x=[]
		if y1==m:x.append(x1)
		if y2==m:x.append(x2)
		if y3==m:x.append(x3)
		print(abs(x[0]-x[1]))
	else:print(0)