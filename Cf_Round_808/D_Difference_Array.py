import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()[::-1];c=0
    while a and a[-1]==0:a.pop();c+=1
    a=a[::-1]
    while True:
        if len(a)==0:print(0);break
        if len(a)==1:print(a[0]);break
        b=[];d=0
        for i in range(len(a)-1):
            if a[i+1]-a[i]>0:b.append(a[i+1]-a[i])
            else:d+=1
        if c>0:b=[a[0]]+b;c-=1
        a=sorted(b);c+=d