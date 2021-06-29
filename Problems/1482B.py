import math;import heapq;import sys
input=sys.stdin.readline
def S():
    return input()
def M():
    return map(int,input().split())
def I():
    return int(S())
def L():
    return list(M())


#start here


for _ in range(I()):
    n=I()
    arr=L()
    dif={arr[i+1]-arr[i] for i in range(n-1)}
    if len(dif)<2:
        print(0)
    elif len(dif)>2:
        print(-1)
    else:
        a,b=sorted(dif)
        if a<0 and b>0 and b-a>max(arr):
            print(b-a,b)
        else:
            print(-1)