import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	if n==1:
		print('a')
	elif n%2==0:
		k=n//2
		print('a'*k+'b'+'a'*(k-1))
	else:
		k=n//2
		print('a'*k+'bc'+'a'*(k-1))