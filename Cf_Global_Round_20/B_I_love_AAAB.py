import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();f=0;c=0
    if s[0]=='B'or s[-1]=='A':print("NO");continue
    for i in range(len(s)):
        if s[i]=='A':c+=1
        if i+1-c>c:f=1;break
    print("NO" if f else "YES")