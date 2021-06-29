import math;import heapq;
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

def ss(x):
	return x[1]

for _ in range(I()):
	n,m,x=M()
	l=L()
	a=[]
	for i in range(m):
		a.append([0,i])
	heapq.heapify(a)
	print("YES")
	for i in range(n):
		t=heapq.heappop(a)
		t[0]+=l[i]
		print(t[1]+1,end=" ")
		heapq.heappush(a,t)
	print()

