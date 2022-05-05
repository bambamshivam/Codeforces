import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();n=len(s);a=[0]*(n+1);b=[0]*(n+1);c=0
    for i in range(n):
        if s[i]=='0':a[i+1]=a[i]+1
        else:a[i+1]=a[i]
    for i in range(n-1,-1,-1):
        if s[i]=='1':b[i]=b[i+1]+1
        else:b[i]=b[i+1]
    for i in range(n):
        if a[i+1]-(s[i]=='0')==0 and b[i]-(s[i]=='1')==0:c+=1
    print(c)