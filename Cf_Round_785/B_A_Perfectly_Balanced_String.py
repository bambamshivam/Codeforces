import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();d=set();f=-1
    for i in range(len(s)):
        if s[i] not in d:d.add(s[i])
        else:f=i;break
    if f==-1:print("YES");continue
    d=s[:f];p=d*(len(s)//f)+d[:len(s)%f]
    print("YES" if p==s else "NO")