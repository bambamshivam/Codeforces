import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    if sum(a)%2==0:print(0);continue
    ans=math.inf
    for i in range(n):
        c=0;p=a[i]%2
        while a[i]%2==p:a[i]//=2;c+=1
        ans=min(ans,c)
    print(ans)