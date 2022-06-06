import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();d={};f=0
    for i in a:d[i]=d.get(i,0)+1
    for i in d:
        if d[i]==1:f=1;break
    if f:print(-1);continue
    i=0;ans=[]
    while i<n:
        j=i+1
        while j<n and a[j]==a[i]:ans.append(j+1);j+=1
        ans.append(i+1);i=j
    print(*ans)