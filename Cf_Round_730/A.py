import math;import heapq;import sys;input=sys.stdin.readline;S=lambda:input();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());H=1000000000+7
for _ in range(I()):
    a,b=M()
    if a==b:
        print(0,0)
    elif a==0 or b==0:
        print(max(a,b),0)
    else:
        t=abs(a-b)
        k=max(a,b)%t
        if k==0:
            print(t,0)
        else:
            print(t,min(k,t-k))
