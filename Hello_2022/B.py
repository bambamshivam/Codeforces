import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();dl={};dr={};d={};mi=math.inf;ma=-1
	for i in range(n):
		l,r,c=M()
		mi=min(mi,l)
		ma=max(ma,r)
		if c<dl.get(l,math.inf):
			dl[l]=c
		if c<dr.get(r,math.inf):
			dr[r]=c
		if c<d.get((l,r),math.inf):
			d[(l,r)]=c
		if (mi,ma) in d:
			print(min(d[(mi,ma)],dl[mi]+dr[ma]))
		else:
			print(dl[mi]+dr[ma])