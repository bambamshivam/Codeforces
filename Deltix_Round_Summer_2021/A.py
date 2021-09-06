import math;import heapq;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
class Solution:
	def main():
		for _ in range(I()):
			c,d=M()
			if c==d and c==0:
				print(0)
			elif c==d:
				print(1)
			elif abs(c-d)%2==1:
				print(-1)
			else:
				print(2)
	if __name__=="__main__":
		main()