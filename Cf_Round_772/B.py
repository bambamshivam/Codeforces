import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	n=I();a=L();c=0;l=[]
	for i in range(1,n-1):
		if a[i-1]<a[i]>a[i+1]:l.append(i)
	i=0
	while i<len(l):
		if i<len(l)-1 and l[i]+2==l[i+1]:
			a[l[i]+1]=max(a[l[i]],a[l[i]+2]);c+=1;i+=2
		else:
			a[l[i]]=max(a[l[i]-1],a[l[i]+1]);c+=1;i+=1
	print(c);print(*a)