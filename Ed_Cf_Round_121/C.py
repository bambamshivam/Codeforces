import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();k=L();h=L();ans=0;l=[]
	for i in range(n):
		l.append([k[i]-h[i]+1,k[i]])
	l.sort()
	for i in range(1,n):
		if max(l[i][0],l[i-1][0])<=min(l[i][1],l[i-1][1]):
			l[i]=[min(l[i][0],l[i-1][0]),max(l[i][1],l[i-1][1])]
			l[i-1]=[-1,-1]
	for i in range(n):
		if l[i][0]!=-1:
			t=l[i][1]-l[i][0]+1
			ans+=t*(t+1)//2
	print(ans)