import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,l,r=M();f=0;ans=[]
    for i in range(1,n+1):
        if l<=(r//i)*i<=r:ans.append((r//i)*i)
        else:f=1;break
    if f:print("NO")
    else:print("YES");print(*ans)