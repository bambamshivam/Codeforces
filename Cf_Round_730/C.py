import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7


def solve(c,m,p,v,s,res,a):
	if len(s)!=0 and s[-1]=="P":
		res[0]+=len(s)*a
		return
	solve(c,m,p,v,s+"P",res,a*p)
	if c>pow(10,-6):
		if c>v:
			k=1
			if m>pow(10,-6):
				k+=1
			x=v/k
			if m>pow(10,-6):
				t=m+x
			else:
				t=m
			solve(c-v,t,p+x,v,s+"C",res,a*c)
		else:
			k=1
			if m>pow(10,-6):
				k+=1
			x=c/k
			if m>pow(10,-6):
				t=m+x
			else:
				t=m
			solve(0,t,p+x,v,s+"C",res,a*c)
	if m>pow(10,-6):
		if m>v:
			k=1
			if c>pow(10,-6):
				k+=1
			x=v/k
			if c>pow(10,-6):
				t=c+x
			else:
				t=c
			solve(t,m-v,p+x,v,s+"M",res,a*m)
		else:
			k=1
			if c>pow(10,-6):
				k+=1
			x=m/k
			if c>pow(10,-6):
				t=c+x
			else:
				t=c
			solve(t,0,p+x,v,s+"M",res,a*m)
 
 
for _ in range(I()):
	c,m,p,v=map(float,input().split())
	res=[0]
	solve(c,m,p,v,"",res,1)
	print(res[0])