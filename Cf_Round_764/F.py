import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

n=I()
l=1;r=n;prev=0
while l+1<r:
	m=(l+r)//2
	print('+',n-m);sys.stdout.flush()
	cur=I()
	if cur>prev:l=m
	else:r=m
	l=(l+n-m)%n;r=(r+n-m)%n
	if r==0:r=n
	prev=cur
print('!',n*prev+l);sys.stdout.flush()