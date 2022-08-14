import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();d={};m=n+1;f=1
    i=0;l=[]
    while i<n:
        j=i+1
        while j<n and a[j]==a[i]:j+=1
        l.append(a[i]);i=j
    a=l[:];n=len(a)
    for i in a:d[i]=d.get(i,0)+1
    for i in range(n-1,-1,-1):
        d[a[i]]-=1
        if d[a[i]]==0 and a[i]<m:m=a[i]
        else:
            d[a[i]]+=1
            ans=0
            for i in d:
                if d[i]>0:ans+=1
            print(ans);f=0;break
    if f:print(0)