import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();p=L();l=[p[i] for i in range(n) if p[i]!=i];ans=l[0]
    for i in range(1,len(l)):ans&=l[i]
    print(ans)