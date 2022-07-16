import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();ans=sum(a[:-1])
    a=a[::-1]
    while a and a[-1]==0:a.pop()
    if len(a)<=1:print(0);continue
    a=a[::-1];n=len(a)
    i=0
    while i<n-1 and a[i]==0:i+=1
    if i==n-1:print(ans);continue
    j=i+1
    while j<n-1 and a[j]!=0:j+=1
    if j==n-1:print(ans);continue
    while True:
        a[i]-=1;ans+=1;a[j]=1
        while i<n-1 and a[i]==0:i+=1
        if i==n-1:break
        j=max(i+1,j+1)
        while j<n-1 and a[j]!=0:j+=1
        if j==n-1:break
    print(ans)