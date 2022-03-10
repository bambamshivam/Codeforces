import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();b=L()
	def f(a,b):
		mab1=min(abs(a[0]-b[i]) for i in range(n))
		mab2=min(abs(a[-1]-b[i]) for i in range(n))
		mba1=min(abs(a[i]-b[0]) for i in range(n))
		mba2=min(abs(a[i]-b[-1]) for i in range(n))
		return (min(mab1+mba1,abs(a[0]-b[0]))+min(mab2+mba2,abs(a[-1]-b[-1])))
	print(min(f(a,b),f(a[::-1],b[::-1]),f(a[::-1],b),f(a,b[::-1])))