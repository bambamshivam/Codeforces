import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();b=L();i=j=0;c=[0]*(n+1);f=1
    while j<n:
        if i<n and j<n and a[i]==b[j]:i+=1;j+=1;continue
        if c[b[j]]>0 and b[j]==b[j-1]:c[b[j]]-=1;j+=1
        elif i<n:c[a[i]]+=1;i+=1
        else:f=0;break
    print("YES" if f else "NO")