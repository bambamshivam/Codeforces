import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	s=input()
	xa,ya=M()
	xb,yb=M()
	xf,yf=M()
	x=abs(xa-xb)
	y=abs(ya-yb)
	if xa==xb==xf and min(ya,yb)<yf<max(ya,yb):
		print(x+y+2)
	elif ya==yb==yf and min(xa,xb)<xf<max(xa,xb):
		print(x+y+2)
	else:
		print(x+y)
