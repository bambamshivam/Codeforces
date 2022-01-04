import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();ans=[0]*n
	def query(i):
		print('?',i+1);sys.stdout.flush()
		return I()
	for i in range(n):
		if ans[i]!=0:continue
		s=set();a=[]
		while 1:
			q=query(i)
			if q in s:break
			a.append(q);s.add(q)
		for j in range(len(a)):
			ans[a[j]-1]=a[(j+1)%len(a)]
	print('!',*ans);sys.stdout.flush()