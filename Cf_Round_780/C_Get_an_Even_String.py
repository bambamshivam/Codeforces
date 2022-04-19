import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();n=len(s);d=[0]*26;ans=0
    for i in s:
        if d[ord(i)-97]:
            ans+=2
            for i in range(26):d[i]=0
        else:d[ord(i)-97]=1
    print(n-ans)