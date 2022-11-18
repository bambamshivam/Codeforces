import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    s=S();ans="YES"
    for i in range(len(s)):
        if s[i] not in "Yes":ans="NO"
    for i in range(len(s)-1):
        if s[i]=='e' and s[i+1]!='s':ans="NO"
        if s[i]=='Y' and s[i+1]!='e':ans="NO"
        if s[i]=='s' and s[i+1]!='Y':ans="NO"
    print(ans)