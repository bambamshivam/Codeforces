import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,k=M();s=S();ans=11*s.count('1')
    if s.count('1')==0:print(0);continue
    if s.count('0')==0:print(n*11-11);continue
    if s.count('1')==1:
        i=s.index('1');j=n-i-1
        if j<=k:print(1)
        elif i<=k:print(10);continue
        else:print(11)
        continue
    i,j=s.index('1'),s[::-1].index('1')
    if j<=k:ans-=10;k-=j
    if i<=k:ans-=1;k-=i
    print(ans)