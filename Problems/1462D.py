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


#start here
for _ in range(I()):
	n=I()
	a=L()
	s=0
	for i in range(n):
		s+=a[i]
		c=0
		for j in range(n):
			c+=a[j]
			if c==s:
				c=0
		if c==0:
			print(n-sum(a)//s)
			break
	if c!=0:
		print(-1)
	
		


