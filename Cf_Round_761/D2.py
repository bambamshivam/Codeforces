import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();l=[];n1=(n//3)
	def query(i,j,k):
		print('?',i+1,j+1,k+1);sys.stdout.flush()
		return I()
	for i in range(n//3):l.append(query(3*i,3*i+1,3*i+2))
	for i in range(n1):
		if l[i]!=l[(i+1)%n1]:break
	p=3*i
	b=[l[i]];b.append(query(p+1,p+2,(p+3)%n));b.append(query(p+2,(p+3)%n,(p+4)%n));b.append(l[(i+1)%n1])
	for i in range(4):
		if b[i]!=b[(i+1)%4]:break
	if b[i]==1:
		a,b=(p+i)%n,(p+i+3)%n
	else:
		a,b=(p+i+3)%n,(p+i)%n
	ans=[b]
	for i in range(n//3):
		d=[3*i,3*i+1,3*i+2]
		if a in d or b in d:
			for k in range(3):
				if d[k] not in [a,b]:
					j=query(a,b,d[k])
					if j==0:ans.append(d[k])
		else:
			if l[i]==0:
				j=query(d[0],d[1],a)
				if j==1:
					ans.append(d[2])
					k=query(d[0],a,b)
					if k==1:ans.append(d[1])
					else:ans.append(d[0])
				else:
					ans.append(d[0]);ans.append(d[1])
					k=query(a,b,d[2])
					if k==0:ans.append(d[2])
			else:
				j=query(d[0],d[1],b)
				if j==0:
					k=query(a,b,d[0])
					if k==1:ans.append(d[1])
					else:ans.append(d[0])
				else:
					k=query(d[2],a,b)
					if k==0:ans.append(d[2])
	for i in range(len(ans)):ans[i]+=1
	print('!',len(ans),*sorted(ans));sys.stdout.flush()