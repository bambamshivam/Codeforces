import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();f1=f2=0
    for i in range(1,n):
        if a[i]==a[i-1]:f1=1;break
    for j in range(n-2,-1,-1):
        if a[j]==a[j+1]:f2=1;break
    if f1+f2==0 or j+1==i:print(0);continue
    print((j-i+1) if j-i==0 else j-i)