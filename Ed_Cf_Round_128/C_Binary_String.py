import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();n=len(s);i=0;j=n-1
    while i<n and s[i]=='0':i+=1
    while j>=0 and s[j]=='0':j-=1
    s=s[i:j+1];n=len(s)
    if s=='1'*n:print(0);continue
    s1=s[1:-1];l=list(s1.split('1'));a=[len(i) for i in l]
    a+=a;n1=len(a)//2;c=s.count('0');p=[0]*(2*n1+1)
    for i in range(len(a)):p[i+1]=p[i]+a[i]
    l=0;r=n1;ans=math.inf
    while l<=r:
        m=(l+r)//2;mx=0
        for i in range(n1-m,n1+1):
            mx=max(mx,p[i+m]-p[i])
        if c-mx<m:ans=min(ans,m);r=m-1
        elif c-mx==m:ans=m;break
        else:ans=min(ans,c-mx);l=m+1
    print(ans)