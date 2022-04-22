import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=L()
    for i in range(n):a[i]%=2
    if a==[0]*n or a==[1]*n:print("YES");continue
    f=1-a[0];ans="YES"
    for i in range(1,n):
        if a[i]!=f:ans="NO";break
        f=1-f
    print(ans)