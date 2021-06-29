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
	l=L()
	di,d={},{}
	c=0
	for i in range(n):
		di[l[i]]=di.get(l[i],0)+1
		d[di[l[i]]]=d.get(di[l[i]],0)+1
	m=-1
	for k in d:
		if k*d[k]>m:
			m=k*d[k]
	print(n-m)
