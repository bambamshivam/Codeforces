import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	s=S()
	l=d=u=r=x=y=0;ans=(0,0);di={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
	for i in range(len(s)):
		a,b=di[s[i]]
		x+=a;y+=b
		l=min(l,y)
		r=max(r,y)
		u=min(u,x)
		d=max(d,x)
		if r-l>=m or d-u>=n:
			break
		ans=(abs(u),abs(l))
	print(ans[0]+1,ans[1]+1)