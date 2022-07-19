import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L();l=[[] for i in range(n+1)];ans=[0]*n
    for i in range(n):l[a[i]].append(i)
    for i in range(1,n+1):
        if len(l[i])==0:continue
        b=[];m=min(len(l[i]),1)
        for j in range(len(l[i])-1):
            b.append(l[i][j+1]-l[i][j])
        j=0;t=len(b);c=d=0
        while j<t:
            if b[j]%2==0:j+=1;continue
            k=j+1;c+=1
            while k<t and b[k]%2:k+=1
            d+=(k-j+1);j=k
        ans[i-1]=d-c+1
    print(*ans)