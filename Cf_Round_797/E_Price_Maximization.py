import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();a=L();l=[[] for i in range(k)];ans=0
    for i in range(n):l[a[i]%k].append(a[i])
    for i in range(1,k//2 +1):
        j=k-i
        m=min(len(l[i]),len(l[j]))
        if i==j:
            m//=2
            for t in range(m):ans+=(l[i].pop()+l[j].pop())//k
            continue
        while j<k:
            m=min(len(l[j]),len(l[i]))
            for t in range(m):ans+=(l[i].pop()+l[j].pop())//k
            if len(l[i])==0:break
            if len(l[j])==0:j+=1
    p=[j for i in range(k) for j in l[i]]
    ans+=sum((p[i]+p[i+1])//k for i in range(0,len(p),2))
    print(ans)