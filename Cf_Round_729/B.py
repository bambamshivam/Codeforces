import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1e9+7
for _ in range(I()):
	n,a,b=M()
	if a==1:
		if (n-1)%b==0:
			print("YES")
		else:
			print("NO")
	else:
		t=1
		f=0
		while t<=n:
			if n%b==t%b:
				f=1
				break
			t*=a
		print("YES") if f==1 else print("NO")


	

	
