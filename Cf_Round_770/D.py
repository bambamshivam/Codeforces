import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I()
	def query(i,j,k,l):
		print('?',i,j,k);sys.stdout.flush()
		a=I()
		print('?',j,k,l);sys.stdout.flush()
		b=I()
		print('?',i,j,l);sys.stdout.flush()
		c=I()
		print('?',i,k,l);sys.stdout.flush()
		d=I()
		s=[{i,j,k},{j,k,l},{i,j,l},{i,k,l}]
		p=0;q=[a,b,c,d];m=max(q);d=[]
		for i in range(4):
			if q[i]==m:
				d.append(s[i]);p+=1
			if p==2:break
		mm=d[0]&d[1]
		return [mm.pop(),mm.pop()]
	l=list(range(1,n+1));c=n
	while c>=4:
		c1=(c//4)*2 + c%4;l1=[]
		for j in range(0,(c//4)*4,4):
			p,q=query(l[j],l[j+1],l[j+2],l[j+3])
			l1.append(p);l1.append(q)
		for j in range((c//4)*4,c):l1.append(l[j])
		l=l1;c=c1
	if c==2:print('!',l[0],l[1]);sys.stdout.flush();continue
	p=1
	for i in range(1,n+1):
		if i not in l:p=i;break
	l.append(p)
	p,q=query(l[0],l[1],l[2],l[3])
	print('!',p,q);sys.stdout.flush()