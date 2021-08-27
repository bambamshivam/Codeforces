import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
	n=I()
	s=S()
	f=0
	a=b=prev=0
	def pal(s):
		m=len(s)
		for i in range(m//2):
			if s[i]!=s[m-i-1]:
				return False
		return True
	while s!='1'*n:
		if pal(s) and n%2==1 and s[n//2]=='0':
			s=s[:n//2]+'1'+s[n//2+1:]
			if f==1:
				b+=1
			else:
				a+=1
			f=1-f
		elif not pal(s) and prev==0:
			prev=1
			s=s[::-1]
			f=1-f
		else:
			j=s.find('0')
			if f==0:
				a+=1
				f=1
			else:
				f=0
				b+=1
			s=s[:j]+'1'+s[j+1:]
	if a>b:
		print("BOB")
	elif a<b:
		print("ALICE")
	else:
		print("DRAW")