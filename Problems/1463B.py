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
	l=L()
	l1,l2=[],[]
	s1,s2=0,0
	for i in range(n):
		if i%2==0:
			l1.append(l[i])
			l2.append(1)
			s1+=l[i]
		else:
			l1.append(1)
			l2.append(l[i])
			s2+=l[i]
	s=s1+s2
	if s1<=s//2:
		print(*l2)
	else:
		print(*l1)

