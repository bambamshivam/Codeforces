import math;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
	n=I();a=L();b=L()
	a=list(enumerate(a))
	b=list(enumerate(b))
	a.sort(key=lambda x:x[1]);b.sort(key=lambda x:x[1])
	la=[0]*n;lb=[0]*n
	for i in range(n):
		la[a[i][0]]=i
		lb[b[i][0]]=i
	a1=a[:];b1=b[:]
	def solve(a,b):
		q=[[a[-1][1],a[-1][0],1]];v=[0]*n;v[a[-1][0]]=1;a.pop()
		while q:
			r,rp,f=q.pop()
			if f==1:
				j=lb[rp]
				if j<len(b):
					for k in range(len(b)-1,j,-1):
						if v[b[k][0]]==0:
							q.append([b[k][1],b[k][0],1-f])
							v[b[k][0]]=1
						b.pop()
					b.pop()
			else:
				j=la[rp]
				if j<len(a):
					for k in range(len(a)-1,j,-1):
						if v[a[k][0]]==0:
							q.append([a[k][1],a[k][0],1-f])
							v[a[k][0]]=1
						a.pop()
					a.pop()
		return v
	v1=solve(a,b);v2=solve(b1,a1)
	s=""
	for i in range(n):s+=str(max(v1[i],v2[i]))
	print(s)