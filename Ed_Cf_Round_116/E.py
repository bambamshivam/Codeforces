import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
n,x=M();h=mod=998244353
dp=[[-1 for j in range(x+1)] for i in range(n+1)]
mx = 505
fac = [1] * mx
for i in range(1, mx):
    fac[i] = fac[i - 1] * i % mod
ifac = [1] * 505
ifac[-1] = pow(fac[-1], mod - 2, mod)
for i in range(mx - 2, 0, -1):
    ifac[i] = (i + 1) * ifac[i + 1] % mod
def C(a, b):
    return fac[a] * ifac[a - b] % mod * ifac[b] % mod
def solve(n,x):
	if x<=0:
		return 0
	if x<n:
		return pow(x,n,h)
	if n==0:
		return 1
	if dp[n][x]<0:
		dp[n][x]=0
		for i in range(n+1):
			dp[n][x]+=((C(n,i)%h)*pow(n-1,i,h)*solve(n-i,x-n+1)%h)%h
	return dp[n][x]%h
print(solve(n,x))