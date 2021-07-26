import math;import heapq;import string;from collections import deque;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
    n,k=M()
    a=L()
    z=[[] for i in range(n)]
    c=[0]*n
    b=0
    j=0
    for i in range(n):
        z[a[i]-1].append(i)
    for i in z:
        b+=min(len(i),k)
    b-=b%k
    for i in z:
        for l in range(min(k,len(i),b)):
            c[i[l]]=j+1
            b-=1
            j+=1
            j%=k
    print(*c)

