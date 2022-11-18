import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    l,r,x=M();a,b=M()
    if not l<=a<=r:print(-1);continue
    if not l<=b<=r:print(-1);continue
    if a==b:print(0);continue
    if abs(a-b)>=x:print(1);continue
    if a>b:a,b=b,a
    if abs(l-a)>=x:print(2);continue
    if abs(r-b)>=x:print(2);continue
    if abs(r-a)>=x and abs(l-b)>=x:print(3);continue
    print(-1);continue