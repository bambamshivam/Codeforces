import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
from collections import deque
n,x=M();q=deque([x]);d={};d[x]=0;f=1
while q:
    r=q.popleft()
    if len(str(r))==n:print(d[r]);f=0;break
    for j in str(r):
        t=r*int(j)
        if t not in d:d[t]=d[r]+1;q.append(t)
if f:print(-1)