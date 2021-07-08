import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

def nxo(a,b,k):
	s=0
	p=1
	while a>0 or b>0:
		c1=a%k
		a=a/k
		c2=b%k
		b=b/k
		t=(c1-c2)%k
		s+=p*t
		p*=k
	return s

for _ in range(I()):
	n,k=M()
	i=0
	while True:
		if i==0:
			q=0
		elif i%2==0:
			q=nxo(i,i-1,k)
		else:
			q=nxo(i-1,i,k)
		print(q)
		sys.stdout.flush()
		r=int(input())
		if r==1:
			break
		i+=1

