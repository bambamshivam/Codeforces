import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
n,q=M()
s=list(S());r=0
for i in range(1,n-1):
	if s[i]=='b' and s[i-1]=='a' and s[i+1]=='c':
		r+=1
for i in range(q):
	p,c=map(str,input().split());p=int(p);p-=1
	if s[p]=='a':
		if p+2<n and s[p+1]=='b' and s[p+2]=='c' and c!='a':
			r-=1
	elif s[p]=='b':
		if p+1<n and p-1>=0 and s[p+1]=='c' and s[p-1]=='a' and c!='b':
			r-=1
	else:
		if p-2>=0 and s[p-2]=='a' and s[p-1]=='b' and c!='c':
			r-=1
	k=s[p];s[p]=c
	if k!=c:
		if s[p]=='a':
			if p+2<n and s[p+1]=='b' and s[p+2]=='c':
				r+=1
		elif s[p]=='b':
			if p+1<n and p-1>=0 and s[p+1]=='c' and s[p-1]=='a':
				r+=1
		else:
			if p-2>=0 and s[p-2]=='a' and s[p-1]=='b':
				r+=1
	print(r)