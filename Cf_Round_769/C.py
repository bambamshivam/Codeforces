import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
	a,b=M();f=0
	if a==b:print(0);continue
	s1=bin(a)[2:];s2=bin(b)[2:]
	s1='0'*(len(s2)-len(s1))+s1
	for i in range(len(s1)):
		if s1[i]=='1' and s2[i]=='0':f=1;break
	if f==0:print(1);continue
	s2=s2[:i]+s1[i:];b1=int(s2,2)
	for j in range(i-1,-1,-1):
		if s1[j]=='0' and s2[j]=='1':
			s1=s1[:j]+'1'+'0'*(len(s2)-j-1);break
	a1=int(s1,2)
	p=a1-a+(a1!=b);q=1+(a|b)-b;r=b1-b+1
	print(min(p,q,r))