import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();f=0
    if n==1:
        if s[0]=='W':print("YES")
        else:print("NO")
        continue
    l=list(s.split('W'))
    for i in l:
        if len(i)>0 and (i=='R'*len(i) or i=='B'*len(i)):f=1;break
    print("NO" if f else "YES")