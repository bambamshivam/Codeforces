import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();ans=1
    for i in range(1,n):
        if s[i]!=s[i-1]:ans+=(i+1)
        else:ans+=1
    print(ans)