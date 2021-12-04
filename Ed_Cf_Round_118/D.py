import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
    n=I()
    a=L()
    dp1,dp2=[0]*(n+2),[0]*(n+2)
    dp1[0]=1
    for i in a:
        dp1[i+1]=(dp1[i+1]*2+dp1[i])%mod2
        if i>0: dp2[i-1]=(dp2[i-1]*2+dp1[i-1])%mod2
        dp2[i+1]=(dp2[i+1]*2)%mod2
    s=0
    for i in dp1+dp2:
        s=(s+i)%mod2
    print((s-1)%mod2)