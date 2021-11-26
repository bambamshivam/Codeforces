import math;from heapq import heappush,heappop,heapify;import random;import string;from collections import deque;from bisect import bisect,bisect_left,bisect_right,insort;import sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000000+7;mod2=998244353
for _ in range(I()):
    n,s=M()
    a=L()
    i=j=0;c=s
    m=-1;p=q=-1
    for k in a:
        c+=k;j+=1
        if c>=0:
            if m<j-i:
                m=j-i
                p,q=i+1,j
        else:
            while c<0:
                c-=a[i]
                i+=1
    if m==-1:
        print(-1)
    else:
        print(p,q)