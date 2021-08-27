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
		ch=pal(s)
		if not ch and prev==0:
			s=s[::-1]
			prev=1
		else:
			if not ch:
				for i in range(n):
					if s[i]=='0' and s[n-i-1]=='1':
						s=s[:i]+'1'+s[i+1:]
						break
			else:
				if n%2==1 and s[n//2]=='0':
					j=n//2
				else:
					j=s.find('0')
				s=s[:j]+'1'+s[j+1:]
			if f==0:
				a+=1 
			else: 
				b+=1
			prev=0
		f=1-f
	if a>b:
		print("BOB")
	elif a<b:
		print("ALICE")
	else:
		print("DRAW")


