import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
prime=[1 for i in range(1000002)]
p=2
while (p*p<=1000001):
    if (prime[p]):
        for i in range(p*p,1000002,p):
            prime[i]=0
    p+=1
for _ in range(I()):
    n,e=M()
    a=L();ans=0
    for i in range(n):
        if a[i]>1 and prime[a[i]]:
            j=i-e;d1=d2=0
            while j>=0 and a[j]==1:
                j-=e;d1+=1
            k=i+e
            while k<n and a[k]==1:
                k+=e;d2+=1
            ans+=d1*d2+d1+d2
    print(ans)