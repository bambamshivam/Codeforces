import math;from heapq import heappush,heappop,heapify;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,m,k=M();l=[]
for i in range(n):
	l.append(L())
a=L()
def nex(i,j,ch):
	if ch==1:
		return (i,j+1)
	elif ch==2:
		return (i+1,j)
	else:
		return (i,j-1)
ans=[]
for i in a:
	t=(0,i-1);c=i-1
	while True:
		s=l[t[0]][t[1]];c=t[1]
		l[t[0]][t[1]]=2
		t=nex(t[0],t[1],s)
		if t[0]>=n or t[0]<0 or t[1]>=m or t[1]<0:
			break
	ans.append(c+1)
print(*ans)