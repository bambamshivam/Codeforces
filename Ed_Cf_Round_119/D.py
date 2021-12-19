import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();l=[[0]*3 for i in range(3)]
	for val in a:
		for i in range(3):
			for j in range(3):
				m=math.inf
				for ii in range(i+1):
					for jj in range(j+1):
						v=val-ii-2*jj
						if v>=0 and v%3==0:
							m=min(m,v//3)
				l[i][j]=max(l[i][j],m)
	print(min(l[i][j]+i+j for i in range(3) for j in range(3)))