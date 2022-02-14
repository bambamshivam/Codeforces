import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

for _ in range(I()):
    n=I();a=L();c=1;p=sorted([0,a[0]-1])
    for i in range(1,n):
        q=sorted([i,a[i]-1])
        if max(p[0],q[0])<=min(p[1],q[1]):
            p=[min(p[0],q[0]),max(p[1],q[1])]
        else:
            p=q[:];c+=1
    print(c)