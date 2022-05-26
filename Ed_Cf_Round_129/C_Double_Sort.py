import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L();ans=[]
    for i in range(n):
        for j in range(i+1,n):
            if a[j]<a[i]:a[j],a[i]=a[i],a[j];b[j],b[i]=b[i],b[j];ans.append([j+1,i+1])
    for i in range(n):
        for j in range(i+1,n):
            if b[j]<b[i]:a[j],a[i]=a[i],a[j];b[j],b[i]=b[i],b[j];ans.append([j+1,i+1])
    if a!=sorted(a):print(-1);continue
    print(len(ans))
    for i in ans:print(*i)