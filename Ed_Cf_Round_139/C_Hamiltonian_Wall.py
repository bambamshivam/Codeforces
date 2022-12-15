import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s1=S();s2=S();l=[s1,s2]
    i=0;cur=0;f=0
    while i<n and s1[i]=='B' and s2[i]=='B':i+=1
    if i<n:
        if s2[i]=='B':cur=1
        i+=1
        while i<n:
            if l[cur][i]!='B':f=1;break
            if l[(cur+1)%2][i]=='B':cur=(cur+1)%2
            i+=1
        print("NO" if f else "YES")
    else:
        print("YES")