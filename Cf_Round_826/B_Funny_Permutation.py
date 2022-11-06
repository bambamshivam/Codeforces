import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I()
    if n==3:print(-1);continue
    if n==2:print(2,1);continue
    l=[n-1]+[n]+list(range(n-2,0,-1))
    r=[n]+[n-1]+list(range(1,n-1))
    if n%2:print(*r)
    else:print(*l)