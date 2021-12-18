import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	w,h=M()
	x1=L()[1:]
	x2=L()[1:]
	y1=L()[1:]
	y2=L()[1:]
	def f(x1,x2,h,y1,y2,d):
		ans=0
		if len(x1)>0:
			if len(x2)>0:
				ans=max(ans,(max(x1)-min(x1))*h)
			else:
				if d==0:
					ans=max(ans,(max(x1)-min(x1))*max(y1+y2))
				else:
					ans=max(ans,(max(x1)-min(x1))*min(y1+y2))
		return ans
	print(max(f(x1,x2,h,y1,y2,0),f(x2,x1,h,y1,y2,1),f(y1,y2,w,x1,x2,0),f(y2,y1,w,x1,x2,1)))