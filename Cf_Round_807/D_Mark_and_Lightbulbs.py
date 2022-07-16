import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353
for _ in range(I()):
    n=I();a=S();b=S()
    if a[0]!=b[0] or a[-1]!=b[-1]:print(-1);continue
    def f(s):
        i=0;p=[];r=[];n=len(s)
        while i<n:
            j=i+1
            while j<n and s[j]==s[i]:j+=1
            r.append([i,j-1])
            p.append(s[i]);i=j
        return [''.join(p),r]
    d=f(a);q=f(b)
    if d[0]==q[0]:
        ans=0
        for i in range(1,len(d[1]),2):
            ans+=(abs(d[1][i][0]-q[1][i][0])+abs(d[1][i][1]-q[1][i][1]))
        print(ans)
    else:print(-1)