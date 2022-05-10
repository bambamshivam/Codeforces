import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();d={};ans=0
    for i in range(n):s=S();d[s]=d.get(s,0)+1
    for i in range(26):
        p=chr(i+97);c=0
        for j in range(26):q=chr(j+97);t=d.get(p+q,0);c+=t;ans-=(t*(t-1)//2)
        ans+=(c*(c-1)//2)
    for i in range(26):
        p=chr(i+97);c=0
        for j in range(26):q=chr(j+97);t=d.get(q+p,0);c+=t;ans-=(t*(t-1)//2)
        ans+=(c*(c-1)//2)
    print(ans)