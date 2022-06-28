import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n,s=M();a=L();p=[-1]*n
    for i in range(n):
        if b[i]!=-1:
            if abs(a[i]-b[i])>s:f=1;break
            s.add(b[i])
    if f:print(0);continue
    for i in range(1,n+1):
        if i not in s:l.append(i)
    