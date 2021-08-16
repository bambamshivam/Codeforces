import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=input().rstrip()
	l=list(s)
	i=0
	while i<n:
		if l[i]=='?':
			i+=1
		elif l[i]=='R':
			a=i-1
			ch='B'
			while a>=0 and l[a]=='?':
				l[a]=ch
				ch='R' if ch=='B' else 'B'
				a-=1
			b=i+1
			ch='B'
			while b<n and l[b]=='?':
				l[b]=ch
				ch='R' if ch=='B' else 'B'
				b+=1
			i=b
		else:
			a=i-1
			ch='R'
			while a>=0 and l[a]=='?':
				l[a]=ch
				ch='R' if ch=='B' else 'B'
				a-=1
			b=i+1
			ch='R'
			while b<n and l[b]=='?':
				l[b]=ch
				ch='R' if ch=='B' else 'B'
				b+=1
			i=b
	if s=='?'*n:
		print('B'*(n%2)+'RB'*(n//2))
	else:
		print("".join(l))


