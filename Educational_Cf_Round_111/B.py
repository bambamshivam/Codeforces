import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,a,b=M()
	s=S()
	if b>=0:
		print(n*(b+a))
	else:
		i=z=o=0
		while i<n:
			j=i+1
			while j<n and s[j]==s[i]:
				j+=1
			if s[i]=='0':
				z+=1
			else:
				o+=1
			i=j
		ans=(min(z,o)+1)*b + n*a
		print(ans)
