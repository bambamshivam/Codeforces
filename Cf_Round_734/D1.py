import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m,k=M()
	if n%2==0 and m%2==0:
		if k%2==0:
			print("YES")
		else:
			print("NO")
	elif n%2==0 and m%2==1:
		k=(n*m)//2 - k
		n,m=m,n
		if k>=(m//2) and (k-(m//2))%2==0:
			print("YES")
		else:
			print("NO")
	else:
		if k>=(m//2) and (k-(m//2))%2==0:
			print("YES")
		else:
			print("NO")
