import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s1=S();s2=S()
    for i in range(n):
        if (s1[i]=='R' and s2[i]!='R') or (s1[i]!='R' and s2[i]=='R'):print("NO");break
    else:print("YES")