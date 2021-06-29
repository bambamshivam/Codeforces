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
	s=""
	if (n-1)%2==0:
		t=(n-1)//2
		k=0
	else:
		t=(n-1)//2 +1
		k=1
	for i in range(n-1,0,-1):
		x=min(i,t-k)
		y=min(k,max(i-x,0))
		z=i-x-y
		s+='1 '*x + '0 '*y + '-1 '*z
	print(s)
