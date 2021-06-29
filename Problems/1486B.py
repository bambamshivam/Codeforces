import math;import heapq
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())


#start here
for _ in range(I()):
	n=I()
	x,y=[],[]
	for i in range(n):
		a,b=M()
		x.append(a)
		y.append(b)
	x.sort()
	nx=len(x)
	a1=x[nx//2] - x[(nx-1)//2] + 1
	y.sort()
	ny=len(y)
	a2=y[ny//2] - y[(ny-1)//2] + 1
	print(a1*a2)