import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=[];d={}
	for i in range(n):l.append(L())
	l.sort(key=lambda x:-(x[1]-x[0]+1))
	for i in l:
		for j in range(i[0],i[1]+1):
			d[j]=d.get(j,0)+1
	for i in range(n):
		a,b=l[i];p=[]
		for j in range(l[i][0],l[i][1]+1):
			d[j]-=1
		for j in range(a,b+1):
			if d[j]==0:
				print(a,b,j);break