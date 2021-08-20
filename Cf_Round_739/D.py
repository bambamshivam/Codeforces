import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7

def lcs(s1,s2):
	n=len(s1)
	m=len(s2)
	j=0
	for i in range(n):
		if j<m and s1[i]==s2[j]:
			j+=1
	return (m-j)+(n-j)
p=1
l=[]
e=pow(10,18)
while p<=e:
	l.append(p)
	p*=2
for _ in range(I()):
	n=I()
	ln=len(str(n))
	m=math.inf
	for i in range(len(l)):
		p=len(str(l[i]))
		temp=lcs(str(n),str(l[i]))
		m=min(temp,m)
	print(m)
	