import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m,k=M()
	if n%2==0 and k%2==1:
		print("NO")
	elif n%2==0 and m%2==0 and k%2==0:
		print("YES")
	elif n%2==0 and m%2==1 and k%2==0:
		if m==1:
			print("NO")
		else:
			print("YES")
	elif n%2==1 and m%2==0 and k%2==0:
		if (k//(m//2))%2==1:
			print("YES")
		else:
			print("NO")
	elif n%2==1 and m%2==0 and k%2==1:
		if k%(m//2)==0 and (k//(m//2))%2==1:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
