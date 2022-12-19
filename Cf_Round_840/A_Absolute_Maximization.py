import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();p=[0]*10;q=[0]*10;x=y=0
    for i in range(n):
        for j in range(10):
            if ((1<<j)&a[i]):p[j]+=1
            else:q[j]+=1
    for i in range(10):
        if p[i]==q[i]==0:continue
        if p[i]>0:x+=(1<<i)
        if q[i]==0:y+=(1<<i)
    print(x-y)