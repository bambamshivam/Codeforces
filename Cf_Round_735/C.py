import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n,m=M()
	m+=1
	bn=str(bin(n))[2:]
	bm=str(bin(m))[2:]
	if len(bn)<len(bm):
		bn='0'*(len(bm)-len(bn))+bn
	else:
		bm='0'*(len(bn)-len(bm))+bm
	s=""
	for i in range(len(bm)):
		if bn[i]=='0' and bm[i]=='1':
			s+='1'
		elif bn[i]=='1' and bm[i]=='0':
			s+='0'*(len(bm)-i)
			break
		else:
			s+='0'
	print(int(s,2))
