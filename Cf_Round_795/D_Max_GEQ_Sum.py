import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();l=L();a=[i for i in l if i!=0];n=len(a);i=f=0
    while i<n and a[i]<0:i+=1
    while i<n:
        j=i+1;s=0
        while j<n and a[j]<0:s+=a[j];j+=1
        if j<n and abs(s)<min(a[i],a[j]):f=1;break
        i=j+1
    for i in range(n-1):
        if a[i]+a[i+1]>max(a[i],a[i+1]):f=1;break
    print("NO" if f else "YES")