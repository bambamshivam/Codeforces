import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000007

lc=1
l=[]
t=10000000000000000
i=1
while lc<=t:
	lc=(lc*i)//math.gcd(lc,i)
	l.append(lc)
	i+=1
for _ in range(I()):
	n=I()
	s=((n%H)*2)%H
	for i in range(1,len(l)):
		if l[i]>n:
			break
		q=(n//l[i])%H
		s=(s+q)%H
	print(s)


