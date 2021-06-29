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
	n,k=M()
	if n-k+1>=k:
		for i in range(k,0,-1):
			print(i,end=" ")
	else:
		for i in range(1,k-(n-k+1)+1):
			print(i,end=" ")
		for i in range(k,k-n+k-1,-1):
			print(i,end=" ")
	print()

