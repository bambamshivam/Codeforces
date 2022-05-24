import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();f=c=0
    for i in range(n//2):
        if s[i]!=s[n-i-1]:f=1;break
    for i in range(n//2 -1,-1,-1):
        if s[i]!=s[n//2]:break
        else:c+=1
    if f:print(1);continue
    print(2*c + (n%2))