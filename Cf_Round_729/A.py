import math;import heapq;import sys
input=sys.stdin.readline
def S():
	return input()
def M():
	return map(int,input().split())
def I():
	return int(S())
def L():
	return list(M())

for _ in range(I()):
	n=I()
	l=L()
	s=0
	f=0
	for i in range(2*n):
		if l[i]%2==0:
			s+=1
		else:
			f+=1
	if s==f:
		print("YES")
	else:
		print("NO")