import math;import heapq
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
    ar=L()
    a=ar.copy()
    a.sort()
    s=[]
    p=a[0]
    k=0
    for i in range (1,n):
        if p<a[i]:
            k=i
        p=p+a[i]
    for i in range (0,n):
        if a[k]<=ar[i]:
            s.append(i+1)
    print(len(s))
    print(*s) 








