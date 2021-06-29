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
	a,b,k=M()
	la=L()
	lb=L()
	d1,d2={},{}
	for i in range(k):
		d1[la[i]]=d1.get(la[i],0)+1
		d2[lb[i]]=d2.get(lb[i],0)+1
	q=0
	for i in range(k):
		q+=k-d1[la[i]]-d2[lb[i]]+1
	print(q//2)


