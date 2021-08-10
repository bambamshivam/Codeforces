import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
class Solution:
	def solve(self,n,l):	
		m=0
		for i in range(n-1):
			m=max(l[i]*l[i+1],m)
		print(m)

	def main(self):
		for _ in range(I()):
			n=I()
			l=L()
			self.solve(n,l)

obj=Solution()
obj.main()