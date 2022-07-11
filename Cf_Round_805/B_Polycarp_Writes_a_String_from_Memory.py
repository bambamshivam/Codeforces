import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();c=set();ans=0
    for i in range(len(s)):
        if len(c)==3 and s[i] not in c:
            ans+=1;c=set();c.add(s[i])
        else:
            c.add(s[i])
    if len(c)>0:ans+=1
    print(ans)