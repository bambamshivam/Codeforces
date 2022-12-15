import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();s=S();d={}
    for i in range(n-1):
        t=d.get(s[i]+s[i+1],[0,-2])
        if i-t[1]>1:d[s[i]+s[i+1]]=[t[0]+1,i]
    for i in d:
        if d[i][0]>1:print("YES");break
    else:print("NO")