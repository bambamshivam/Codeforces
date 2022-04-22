import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,x=M();a=L();m1=min(a);m2=max(a)
    ans=sum(abs(a[i]-a[i+1]) for i in range(n-1))
    if m1==1 and m2<x:
        m=min(abs(a[0]-x),abs(a[-1]-x))
        for i in range(1,n-1):
            if a[i]==m2:
                m=min(abs(a[i-1]-x)+abs(a[i]-x)-abs(a[i]-a[i-1]),abs(a[i+1]-x)+abs(a[i]-x)-abs(a[i]-a[i+1]),m)
        ans+=m
    elif m1!=1:
        if m2>=x:
            m=min(abs(a[0]-1),abs(a[-1]-1))
            for i in range(1,n-1):
                if a[i]==m1:
                    m=min(abs(a[i-1]-1)+abs(a[i]-1)-abs(a[i]-a[i-1]),abs(a[i+1]-1)+abs(a[i]-1)-abs(a[i]-a[i+1]),m)
            ans+=m
        else:
            m=min(abs(a[0]-x),abs(a[-1]-x))
            for i in range(1,n-1):
                if a[i]==m2:
                    m=min(abs(a[i-1]-x)+abs(a[i]-x)-abs(a[i]-a[i-1]),abs(a[i+1]-x)+abs(a[i]-x)-abs(a[i]-a[i+1]),m)
            ans+=m
            m=min(abs(a[0]-1),abs(a[-1]-1))
            for i in range(1,n-1):
                if a[i]==m1:
                    m=min(abs(a[i-1]-1)+abs(a[i]-1)-abs(a[i]-a[i-1]),abs(a[i+1]-1)+abs(a[i]-1)-abs(a[i]-a[i+1]),m)
            ans+=m
    print(ans)