import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n=I()
l=[]
for i in range(n):
	a=L()
	l.append(a[1:])
m=I()
di={}
for i in range(m):
	a=L()
	s=""
	for j in a:
		s+=str(j)
	di[s]=1
d=[]
heapq.heapify(d)
s=""
for i in range(n):
	if len(l[i])>1:
		x=(l[i][-1]-l[i][-2],len(l[i])-1,i)
		heapq.heappush(d,x)
	else:
		x=(math.inf,len(l[i])-1,i)
		heapq.heappush(d,x)
	s+=str(len(l[i]))
while di.get(s,-1)!=-1:
	i=heapq.heappop(d)
	t=i[-1]
	s=s[:t]+str(int(s[t])-1)+s[t+1:]
	if int(s[t])==0:
		x=(math.inf,0,t)
		heapq.heappush(d,x)
	else:
		p=int(s[t])
		x=(l[t][p]-l[t][p-1],i[-2]-1,t)
		heapq.heappush(d,x)
for i in range(len(s)):
	print(s[i],end=" ")
print()