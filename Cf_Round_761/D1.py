import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=[]
	def query(i,j,k):
		print('?',i+1,j+1,k+1);sys.stdout.flush()
		return I()
	for i in range(n):l.append(query(i,(i+1)%n,(i+2)%n))
	for i in range(n):
		if l[i]!=l[(i+1)%n]:break
	if l[i]==1:
		a,b=i,(i+3)%n
	else:
		a,b=(i+3)%n,i
	ans=[b+1]
	for i in range(n):
		if i!=a and i!=b:
			j=query(a,b,i)
			if j==0:ans.append(i+1)
	print('!',len(ans),*sorted(ans));sys.stdout.flush()